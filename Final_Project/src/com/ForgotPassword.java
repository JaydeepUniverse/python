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

public class ForgotPassword extends HttpServlet {
    protected void service(HttpServletRequest req, HttpServletResponse res) throws IOException, ServletException {
	String first_name = req.getParameter("first_name");
	int mobile_no = Integer.parseInt(req.getParameter("mobile_no"));
	String email_id = req.getParameter("email_id");
	String user_validate = "select * from users where mobile_no='" + mobile_no + "' and email_id='" + email_id + "' and first_name='" + first_name + "'";
	
	
	try {
	    Class.forName("com.mysql.jdbc.Driver");
	    Connection c = DriverManager.getConnection("jdbc:mysql://localhost:3306/project", "root", "devops");
	    PreparedStatement p = c.prepareStatement(user_validate);
	    ResultSet r = p.executeQuery();
	    System.out.println("in try condition");
	    if (r.next()) {
		do {
		    System.out.println("stating of while condition");
		    if (mobile_no == r.getInt("mobile_no") && email_id.equals(r.getString("email_id")) && first_name.equals(r.getString("first_name"))) {
			System.out.println("in if condition");
			Cookie ck = new Cookie("mobile_no", mobile_no+"");
			res.addCookie(ck);
			res.sendRedirect("ResetPassword.html");
		    }

		} while (r.next());
	    } else {
		System.out.println("in else condition");
		RequestDispatcher rd = null;
		PrintWriter out = res.getWriter();
		out.write("<p id='forgotPassword' style='color: red; font-size: larger;'>either mobile no. OR emaild OR first name is incorrect</p>");
		rd = req.getRequestDispatcher("ForgotPassword.html");
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