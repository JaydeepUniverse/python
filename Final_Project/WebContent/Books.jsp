<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<%@ taglib uri="http://java.sun.com/jsp/jstl/sql" prefix="sql"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>

<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Book Store - Books</title>
<script type="text/javascript" src="js/jquery-1.8.0.min.js"></script>

<script type="text/javascript">
	$(document).ready(function() {
		$('#mobile_no, #password').click(function() {
			$("#loginMessage").hide();
		});
	});
</script>

</head>
<body>
	<h2>Available Books :</h2>
	<sql:setDataSource var="snapshot" driver="com.mysql.jdbc.Driver"
		url="jdbc:mysql://localhost:3306/project" user="root"
		password="devops" />
	<sql:query dataSource="${snapshot}" var="result">
         select book_name from books;
      </sql:query>
      <form action="book_select" method="post">
		<table border="1" width="50%">
			<c:forEach var="row" items="${result.rows}">
				<tr>
					<td style="width:10px;" align="center" >
					<input type="checkbox" name="selected_items" value="<c:out value="${row.Book_Name}" />"  />
					</td>
					<td align="left" >
					
					<input type="text" name="<c:out value="${row.Book_Name}" />" value="${row.Book_Name}" style="width:500px;"/>
					</td>
				</tr>
			</c:forEach>
			<tr>
				<td><input type="submit" value="Register book to purchase"></td>
			</tr>

		</table>
		</form>
</body>
</html>

