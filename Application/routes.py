from DataBaseTools.getStockPrice import getStockPrice
from Application import app
from flask import render_template, request, session, g, redirect, url_for, flash
from User import User, login_required

from FigureGenerator import Figure
from FigureGenerator.Traces.ScatterTrace import ScatterTrace
from FigureGenerator.Traces.BarTrace import BarTrace
from FigureGenerator.Traces.LineTrace import LineTrace
from FigureGenerator.Traces.ScatterLineTrace import ScatterLineTrace
from FigureGenerator.Traces.CandleStickTrace import CandleStickTrace
from DataBaseTools.getCompanies import getCompanies
from DataBaseTools import technicalAn


@app.route("/")
# @login_required    #by uncommenting this,you can force user to sign in to access this page
def index():
    select = getCompanies()
    return render_template("index.html", options1=select)


@app.route("/candleStickChart", methods=['GET', 'POST'])
def candleStickChart():
    select = getCompanies()
    name = request.args.get('company')
    indicators = request.args.getlist('indicators')
    df = getStockPrice(name)

    fig = Figure()
    fig.set_Title("%s stock history" % (name))
    fig.set_xLabel("Date")
    fig.set_yLabel("Price")

    trace = CandleStickTrace()
    trace.set_name(name)
    x_values = df["Date"].tolist()
    trace.add_X_values(df["Date"].tolist())
    trace.add_open_values(df["Open"].tolist())
    trace.add_low_values(df["Low"].tolist())
    trace.add_high_values(df["High"].tolist())
    trace.add_close_values(df["Close"].tolist())
    trace.set_increasing_line_color("green")
    trace.set_decreasing_line_color("red")

    fig.add_trace(trace)

    fig2 = Figure()
    fig2.set_xLabel("Date")
    fig2.set_yLabel("Volume")

    volTrace = BarTrace()
    volTrace.add_X_values(df["Date"].tolist())
    volTrace.add_Y_values(df["Volume"].tolist())
    volTrace.set_color("blue")
    volTrace.set_name("Volume")

    fig2.add_trace(volTrace)
    if indicators is not None:
        print(indicators)
        for indicator in indicators:
            if indicator == 'BB':
                df = technicalAn.BB(name)
                upper_band, lower_band, moving_average = technicalAn.handleRequest(
                    x_values, df, 'BB')
                fig.add_trace(upper_band)
                fig.add_trace(lower_band)
                fig.add_trace(moving_average)

            elif indicator == 'RSI':
                df = technicalAn.RSI(name)
                rsi = technicalAn.handleRequest(x_values, df, 'RSI')
                fig.add_trace(rsi)

            elif indicator == 'ATR':
                df = technicalAn.ATR(name)
                atr = technicalAn.handleRequest(x_values, df, 'ATR')
                fig.add_trace(atr)

            elif indicator == 'MA':
                window = request.args.get('indicators_ma')
                if window is None:
                    window = 2
                window = int(window)
                df = technicalAn.movingAverage(name, window)
                ma = technicalAn.handleRequest(x_values, df, 'MA')
                fig.add_trace(ma)

            elif indicator == 'EMA':
                window = request.args.get('indicators_ema')
                if window is None:
                    window = 2
                window = int(window)
                df = technicalAn.exponentialMovingAverage(name, window)
                ma = technicalAn.handleRequest(x_values, df, 'EMA')
                fig.add_trace(ma)

    return render_template("figures.html",
                           title="%s stock data" % (name),
                           figure1=fig.render(),
                           figure2=fig2.render(),
                           figure3=df,
                           company=name,
                           options1=select
                           )


@app.route("/login", methods=('GET', 'POST'))
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['pass']

        user = User()
        if(user.login(username, password)):
            session.clear()
            session['user_id'] = user.get_id()
            return redirect(url_for('index'))
        else:
            flash("Incorrect username or password", "error")

    return render_template("login.html")


@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))


@app.route("/register", methods=('GET', 'POST'))
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        passCheck = request.form['password2']
        firstname = request.form['fname']
        lastname = request.form['lname']
        email = request.form['email']

        user = User()

        if(password != passCheck):
            flash("Passwords don't match", "error")
        elif(user.register(firstname, lastname, username, email, password)):
            session.clear()
            session['user_id'] = user.get_id()
            return redirect(url_for('index'))

    return render_template("register.html")

# this means this function will run before all other route functions( suppose you open index page, this runs then the index function runs)


@app.before_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = User()
        g.user.load_user_id(user_id)
