'''
useful : 1

原始代码如下所示，请注意:
1）原始的注释和代码存在于多行注释中，改造后的代码应该写在注释以外，并保证代码不会出现依赖错误；
2）如果代码因为无法改造导致的无法使用，请不用在注释外添加内容，且将注释开头的useful标注为0；
3）代码改造以后尽量保证代码美观和缩进信息正确，且一次缩进为4个空格；
4）可以对注释中的代码进行修改，但最终改造结果需要保存在注释以外。

comment:
Book a flight.


code:
def book():
Book a flight.

    # Get form information.
    name = request.form.get('name')

    # Make sure that the flight id is a number (in case of a weird error).
    try:
        flight_id = int(request.form.get('flight_id'))
    except ValueError:
        return render_template('error.html', message='Invalid flight number.')

    # Make sure flight exists.
    if db.execute('SELECT * FROM flights WHERE id = :id', {'id': flight_id}).rowcount == 0:
        return render_template('error.html', message='No such flight with that id.')

    # If the flight exists, record the passenger as having registered for the flight.
    db.execute('INSERT INTO passengers (name, flight_id) VALUES (:name, :flight_id)',
            {'name': name, 'flight_id': flight_id})

    # All done booking!
    db.commit()
    return render_template('success.html')
'''
# 尝试性使用$conn$查询passengers表中flight_id为$flight_id$的所有name，渲染并返回'success.html'，其中text参数为查询结果。如果出现ValueError，则渲染'error.html'，传入message参数为'Invalid flight number.'
from flask import render_template
def book(conn,flight_id):
    try:
        texts = conn.execute("SELECT name FROM passengers WHERE flight_id=:flight_id",{"flight_id":flight_id}).fetchall()
        return render_template('success.html', text = texts)
    except ValueError:
        return render_template('error.html', message='Invalid flight number.')