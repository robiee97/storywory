package com.example.MainApp.services;

import com.example.MainApp.dtos.PostDto;
import com.example.MainApp.models.Owner;
import com.example.MainApp.models.Post;
import com.example.MainApp.repositories.PostRepository;
import lombok.AllArgsConstructor;
import lombok.NoArgsConstructor;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;

import java.util.List;

@Service
@AllArgsConstructor
public class PostService {

    private PostRepository postRepository;

    public void savePost(PostDto postDto){
        Post post= new Post();
        post.setId(postDto.getId());
        Owner owner=new Owner();
        owner.setUsername(postDto.getOwner().getUsername());
        owner.setProfile_pic(postDto.getOwner().getProfile_pic());
        post.setOwner(owner);
        post.setPhoto(postDto.getPhoto());
        post.setText(postDto.getText());
        post.setLocation(postDto.getLocation());
        post.setPosted_on(postDto.getPosted_on());
        post.setNumber_of_likes(postDto.getNumber_of_likes());

        postRepository.save(post);
        System.out.println("post saved in DB");
    }

    public List<Post> getAllPosts(){
        return postRepository.findAll();
    }
}
