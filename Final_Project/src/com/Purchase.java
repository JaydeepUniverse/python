package com;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.HashMap;
import java.util.Map;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class Purchase extends HttpServlet {
    protected void service(HttpServletRequest req, HttpServletResponse res) throws IOException, ServletException {
	int quantity = Integer.parseInt(req.getParameter("quantity"));
	String password = req.getParameter("password");
	String user_validate = "select * from users where mobile_no='" + mobile_no + "' and password='" + password
		+ "'";

	try {
	    Class.forName("com.mysql.jdbc.Driver");
	    Connection c = DriverManager.getConnection("jdbc:mysql://localhost:3306/project", "root", "devops");
	    PreparedStatement p = c.prepareStatement(user_validate);
	    ResultSet r = p.executeQuery();
	    System.out.println("in try condition");
	    if (r.next()) {
		do {
		    System.out.println("stating of while condition");
		    if (mobile_no == r.getInt("mobile_no") && password.equals(r.getString("password"))) {
			System.out.println("in if condition");
			RequestDispatcher rd = null;
			PrintWriter out = res.getWriter();
			out.write("<p id='loginMessage' style='color: green; font-size: larger;'>Welcome! Login Sucessful</p>");
			rd = req.getRequestDispatcher("Books.jsp");
			rd.include(req, res);
		    }

		} while (r.next());
	    } else {
		System.out.println("in else condition");
		RequestDispatcher rd = null;
		PrintWriter out = res.getWriter();
		out.write("<p id='loginMessage' style='color: red; font-size: larger;'>either mobile no. OR password is incorrect</p>");
		rd = req.getRequestDispatcher("Welcome.jsp");
		rd.include(req, res);
	    }
	    System.out.println("ending of while condition");

	    c.close();
	} catch (SQLException e) {
	    e.printStackTrace();
	} catch (ClassNotFoundException e) {
	    // TODO Auto-generated catch block
	    e.printStackTrace();
	}
	System.out.println("in main service method");
    }
}