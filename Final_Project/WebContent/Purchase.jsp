<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
	pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<%@ taglib uri="http://java.sun.com/jsp/jstl/sql" prefix="sql"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@page import="com.Book_Details"%>
<%@page import="java.util.ArrayList"%>

<html>
<head>
<script type="text/javascript">
function calculate() {

var USERINPUT1 = document.getElementById("input").value;
var USERINPUT2 = document.getElementById("input").value;
var CALC1 = USERINPUT1 + USERINPUT2;
document.getElementById("output").innerHTML = CALC1;

}
</script>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Book Store - Selected Books</title>

</head>
<form name="book_selected" action="purchase" method="post">
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
		    for(book_details s:bk) {
			   
		
		 
		%>

		<tr>
			<td><%=s.getId()%></td>
			<td><%=s.getBook_name()%></td>
			<td><%=s.getAuthor()%></td>
			<td><%=s.getPrice()%></td>
			<td><input id="input" type="number" name="INPUT1" value="" onchange="calculate();" required></td>
		</tr>
		<!-- <tr>
			<td><input type="submit" value="Purchase"></td>
		</tr> -->
		
		<%
		    }
		%>
	</table>
	<input id="output" type="number" name="OUTPUT1">
	<input type="button" onclick="calculate();" value="Add"/>
	<!-- <input type="submit" value="Purchase"> -->
</form>
</body>
</html>