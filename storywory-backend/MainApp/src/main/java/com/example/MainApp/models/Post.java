package com.example.MainApp.models;

import com.fasterxml.jackson.annotation.JsonFormat;
import lombok.AllArgsConstructor;
import lombok.Builder;
import lombok.Data;
import lombok.NoArgsConstructor;
import org.springframework.data.annotation.Id;
import org.springframework.data.mongodb.core.mapping.Document;

import java.sql.Timestamp;
import java.util.Date;


@Data
@NoArgsConstructor
@AllArgsConstructor
@Builder
@Document(collection = "Post")
public class Post {
        @Id
    	private String id;
        private Owner owner;
	    private String photo;
        private String text;
        private String location;
        private Date posted_on;
        private Integer number_of_likes;
}
