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
//        if(productRepository.existsById(productDto.getId())){
//            productService.update(productDto,productDto.getId());
//        }else{
//            productService.create(productDto);
//        }
        postService.savePost(postDto);
    }
//    @KafkaListener(topics = {"product_deleted"},groupId = "myId",containerFactory = "kafkaListenerContainerFactory")
//    public void listen(String data){
//        Long id=Long.parseLong(data.substring(1,data.length()-1));
//        if(productRepository.existsById(id)){
//            productService.delete(id);
//        }else{
//            System.out.println("Product Not found");
//        }
//    }

}
