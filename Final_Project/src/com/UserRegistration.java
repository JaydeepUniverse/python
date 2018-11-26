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
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

public class UserRegistration extends HttpServlet {
    protected void service(HttpServletRequest req, HttpServletResponse res) throws IOException, ServletException {
	String first_name = req.getParameter("first_name");
	int mobile_no = Integer.parseInt(req.getParameter("mobile_no"));
	String password = req.getParameter("password");
	String email_id = req.getParameter("email_id");
	String address = req.getParameter("address");
	int pin_code = Integer.parseInt(req.getParameter("pin_code"));

	try {
	    Class.forName("com.mysql.jdbc.Driver");
	    Connection c = DriverManager.getConnection("jdbc:mysql://localhost:3306/project", "root", "devops");
	    PreparedStatement p = c.prepareStatement("insert into users values(?,?,?,?,?,?)");
	    p.setString(1, first_name);
	    p.setInt(2, mobile_no);
	    p.setString(3, password);
	    p.setString(4, email_id);
	    p.setString(5, address);
	    p.setInt(6, pin_code);
	    p.executeUpdate();
	    c.close();
	} catch (ClassNotFoundException e) {
	    e.printStackTrace();
	} catch (SQLException e) {
	    e.printStackTrace();
	}
	PrintWriter out = res.getWriter();
	out.write("<p id='welcomeMessage' style='color: green; font-size: larger;'>Welcome! Your registration has been successful</p>");
	RequestDispatcher rd = null;
	rd = req.getRequestDispatcher("Welcome.jsp");
	rd.include(req, res);
    }
}