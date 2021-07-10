package com.example.MainApp.controllers;

import com.example.MainApp.dtos.PostDto;
import com.example.MainApp.models.Post;
import com.example.MainApp.services.PostService;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@RestController
@RequestMapping("/post")
@AllArgsConstructor
public class PostController {

    private PostService postService;

    @GetMapping("/")
    public ResponseEntity<List<Post>> getAllPosts(){
        return new ResponseEntity(postService.getAllPosts(), HttpStatus.OK);
    }
}
