#!/usr/bin/ruby

print "Content-type: text/html\n\n"

require "cgi"
require "date"
require "mysql"

cgi = CGI.new

# connect to DB
dbconnect = Mysql::new("localhost","root","ogiman","ogimandb")

insert_name = cgi["your name"]
select_feel = cgi["feeling"]


# output image "2018/03/16 22:56:45"
time = Time.now
now  = time.strftime("%Y/%m/%d %H:%M:%S")

dbconnect.query(
    "INSERT INTO `ogimantable`(
        `date`, `name`, `feel`)
    VALUES(
        '#{now}','#{insert_name}','#{select_feel}');"
    )

query_result=dbconnect.query("select * from ogimantable")

# #DBの値を表示
# res.each_hash do |row|
#   p row
# end

print <<OK
<html>
 </body>
 <h2>ogiman</h2>

 <table border="3">
  <tr>
    <th>ID</th>
    <th>DATE</th>
    <th>NAME</th>
    <th>FEEL</th>
  </tr>
OK

query_result.each do |row|
    print "<tr>"
    print "<td>#{row[0]}</td>"
    print "<td>#{row[1]}</td>"
    print "<td>#{row[2]}</td>"
    print "<td>#{row[3]}</td>"
    print "</tr>"
end


print "<table>"
print "</body></html>"

