package com.example.MainApp.services;

import com.example.MainApp.dtos.PostDto;
import com.example.MainApp.exceptions.CustomExceptions;
import com.example.MainApp.models.Owner;
import com.example.MainApp.models.Post;
import com.example.MainApp.repositories.PostRepository;
import lombok.AllArgsConstructor;
import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;
import java.util.stream.Collectors;

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

    public List<Post> getPostsByText(String text){
        List<Post>list= postRepository.findAll();
        List<Post> res=list.stream().filter(post->post.getText().equals(text)).collect(Collectors.toList());
        return res;
    }

    public List<Post> getPostsByLocation(String location){
        List<Post>list= postRepository.findAll();
        List<Post> res=list.stream().filter(post->post.getLocation().equals(location)).collect(Collectors.toList());
        return res;
    }

    public ResponseEntity<String> likepostAPI(String id){
        Post post=postRepository.findById(id).orElseThrow(()-> new CustomExceptions("post not found"));
        post.setNumber_of_likes(post.getNumber_of_likes()+1);
        postRepository.save(post);
        return new ResponseEntity<>("liked", HttpStatus.OK);
    }
    public ResponseEntity<String> dislikepostAPI(String id){
        Post post=postRepository.findById(id).orElseThrow(()-> new CustomExceptions("post not found"));
        post.setNumber_of_likes(post.getNumber_of_likes()-1);
        postRepository.save(post);
        return new ResponseEntity<>("disliked", HttpStatus.OK);
    }

}
