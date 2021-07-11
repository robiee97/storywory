package com.example.MainApp.consumers;

import com.example.MainApp.dtos.PostDto;
import com.example.MainApp.repositories.PostRepository;
import com.example.MainApp.services.PostService;
import lombok.AllArgsConstructor;
import org.springframework.kafka.annotation.KafkaListener;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;

@Service
@Component
@AllArgsConstructor
public class PostConsumer {

    private PostService postService;
    private PostRepository postRepository;

    @KafkaListener(topics = {"Addpost"},groupId = "myId",containerFactory ="postKafkaListenerContainerFactory")
    public void listen(PostDto postDto){
        postService.savePost(postDto);
    }
}
