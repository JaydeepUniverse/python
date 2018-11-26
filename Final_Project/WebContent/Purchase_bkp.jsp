<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<%@ taglib uri="http://java.sun.com/jsp/jstl/sql" prefix="sql"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>

<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Book Store - Books</title>

</head>
<body>
	<h2>Book Details :</h2>
	<table border="1" width="80%">
		<tr>
			<td>Book_ID</td>
			<td>Book_Name</td>
			<td>Author</td>
			<td>Price</td>
		</tr>
		<tr>
			<td><%=request.getAttribute("book_id")%></td>
			<td><%=request.getAttribute("book_name")%></td>
			<td><%=request.getAttribute("author")%></td>
			<td><%=request.getAttribute("price")%></td>
		</tr>
	</table>


</body>
</html>