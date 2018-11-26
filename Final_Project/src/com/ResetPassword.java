package com;

import java.io.IOException;
import java.io.PrintWriter;
import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.ResultSet;
import java.sql.Statement;

import javax.servlet.RequestDispatcher;
import javax.servlet.ServletException;
import javax.servlet.http.Cookie;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;

import org.apache.jasper.tagplugins.jstl.core.Out;

public class ResetPassword extends HttpServlet {
    protected void doPost(HttpServletRequest req, HttpServletResponse res) throws ServletException, IOException {
	try {
	    String password = req.getParameter("setPassword");
	    //PrintWriter out = res.getWriter();
	    Cookie ck[] = req.getCookies();
	    //out.print("Hello " + ck[0].getValue());
	    //out.close();
	    int mobile_no = Integer.parseInt(ck[0].getValue());
	    String update_password = "update users set password='" + password + "' where mobile_no='" + mobile_no + "'";
	    String verify_update_password = "select * from users where mobile_no='" + mobile_no + "'";
	    Class.forName("com.mysql.jdbc.Driver");
	    Connection c = DriverManager.getConnection("jdbc:mysql://localhost:3306/project", "root", "devops");
	    Statement s = c.createStatement();
	    s.executeUpdate(update_password);
	    ResultSet r = s.executeQuery(verify_update_password);
	    while(r.next())
		System.out.println(r.getString(1) + " " + r.getInt(2) + " " + r.getString(3) + " " + r.getString(4) + " " + r.getString(5) + " " + r.getInt(6));
	    c.close();
	    RequestDispatcher rd = null;
		PrintWriter out = res.getWriter();
		out.write("<p id='forgotPassword' style='color: green; font-size: larger;'>password reset successfully</p>");
		rd = req.getRequestDispatcher("Welcome.jsp");
		rd.include(req, res);
//	    res.sendRedirect("Welcome.jsp");
	} catch (Exception e) {
	    System.out.println(e);
	}
    }
}
