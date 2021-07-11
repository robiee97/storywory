package com.example.MainApp.controllers;

import com.example.MainApp.dtos.PostDto;
import com.example.MainApp.models.Post;
import com.example.MainApp.services.PostService;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.client.RestTemplate;

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
    @GetMapping("/text/{keyword}")
    public ResponseEntity<List<Post>> getPostsByText(@PathVariable String keyword){
        return new ResponseEntity(postService.getPostsByText(keyword), HttpStatus.OK);
    }
    @GetMapping("/location/{keyword}")
    public ResponseEntity<List<Post>> getPostsByLocation(@PathVariable String keyword){
        return new ResponseEntity(postService.getPostsByLocation(keyword), HttpStatus.OK);
    }


    /*called by DRF*/
    @PostMapping("/like/{id}")
    public ResponseEntity<String> likepost(@PathVariable String id){
        return postService.likepostAPI(id);
    }
    @PostMapping("/dislike/{id}")
    public ResponseEntity<String> dislikepost(@PathVariable String id){
        return postService.dislikepostAPI(id);
    }

}
