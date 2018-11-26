package com;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class BookSelect_bkp extends HttpServlet {
       protected void service(HttpServletRequest req, HttpServletResponse res) throws IOException, ServletException {
	   
	String selected_book = req.getParameter("selected_book");
	String find_book = "select * from books where book_name=\"" + selected_book + "\"";

	System.out.println(selected_book);
	
	try {

	    Class.forName("com.mysql.jdbc.Driver");
	    Connection c = DriverManager.getConnection("jdbc:mysql://localhost:3306/project", "root", "devops");
	    Statement s = c.createStatement();
	    ResultSet r = s.executeQuery(find_book);
	    System.out.println("in try condition");
	    while(r.next()) {
		req.setAttribute("book_id", r.getInt(1));
		req.setAttribute("book_name", r.getString(2));
		req.setAttribute("author", r.getString(3));
		req.setAttribute("price", r.getInt(4));
		System.out.println(r.getInt(1) + " " + r.getString(2) + " " + r.getString(3) + " " + r.getInt(4));		
	    }
	    RequestDispatcher view = req.getRequestDispatcher("Purchase.jsp");  
	    view.forward(req,res);  
	    System.out.println("ending of while condition");
	    c.close();
	    
	} catch (SQLException e) {
	    e.printStackTrace();
	} catch (ClassNotFoundException e) {
	    e.printStackTrace();
	}
	System.out.println("in main service method");
    }
    
}