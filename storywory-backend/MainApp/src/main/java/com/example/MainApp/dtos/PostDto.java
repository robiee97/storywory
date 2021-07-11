package com.example.MainApp.dtos;

import com.example.MainApp.models.Owner;
import com.fasterxml.jackson.annotation.JsonFormat;
import lombok.AllArgsConstructor;
import lombok.Data;
import lombok.NoArgsConstructor;

import java.sql.Timestamp;
import java.util.Date;

@Data
@AllArgsConstructor
@NoArgsConstructor
public class PostDto {
    private String id;
    private Owner owner;
    private String photo;
    private String text;
    private String location;
    private Date posted_on;
    private Integer number_of_likes;
}
