package com.example.MainApp.repositories;

import com.example.MainApp.models.Post;
import org.springframework.data.mongodb.repository.MongoRepository;

public interface PostRepository extends MongoRepository<Post,String> {

}
