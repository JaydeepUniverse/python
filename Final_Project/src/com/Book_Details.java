package com;

public class Book_Details {
    private int id;
    private String book_name;
    private String author;
    private int price;
    
    public Book_Details(int i, String b, String a, int p) {
	this.id = i;
	this.book_name = b;
	this.author = a;
	this.price = p;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getBook_name() {
        return book_name;
    }

    public void setBook_name(String book_name) {
        this.book_name = book_name;
    }

    public String getAuthor() {
        return author;
    }

    public void setAuthor(String author) {
        this.author = author;
    }

    public int getPrice() {
        return price;
    }

    public void setPrice(int price) {
        this.price = price;
    }
    
    
}
