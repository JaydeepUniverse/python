<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<%@ taglib uri="http://java.sun.com/jsp/jstl/sql" prefix="sql"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@page import="com.Book_Details"%>
<%@page import="java.util.ArrayList"%>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Book Store - Selected Books</title>

</head>
<form action="purchase" method="post">
	<table border="1" width="500">
		<tr>
			<th><b>Book ID</b></th>
			<th><b>Book Name</b></th>
			<th><b>Author</b></th>
			<th><b>Price</b></th>
			<th><b>Quantity</b>
		</tr>
		<%
		    ArrayList<Book_Details> bk = (ArrayList<Book_Details>) request.getAttribute("selected_books");
		    for (Book_Details s : bk) {
		%>

		<tr>
			<td><%=s.getId()%></td>
			<td><%=s.getBook_name()%></td>
			<td><%=s.getAuthor()%></td>
			<td><%=s.getPrice()%></td>
			<td><form oninput="parseInt(a.value)+parseInt(b.value)">
					<input type="number" id="a" >
					<input type="number" id="b" > =
					<output name="x" for="a b"></output>
				</form></td>
		</tr>
		<tr>
			<td><input type="submit" value="Purchase"></td>
		</tr>
		<%
		    }
		%>
	</table>
</form>
<%-- <h2>Book Details :</h2>
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
	</table> --%>


</body>
</html>