package com.example.MainApp.exceptions;

public class CustomExceptions extends  RuntimeException {
    public CustomExceptions(String s, Exception e) {
        super(s,e);
    }
    public CustomExceptions(String s) {
        super(s);
    }


}
