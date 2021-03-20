from flask import render_template

        texts = conn.execute("SELECT name FROM passengers WHERE flight_id=:flight_id",{"flight_id":flight_id}).fetchall()