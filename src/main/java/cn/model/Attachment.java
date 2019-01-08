/**
 * Created by Steudnera 
 */
package com.muffino.model;

import com.blog.model.File;
import com.blog.model.User;
import com.blog.model.Content;
import com.blog.model.Authority;

import java.sql.Timestamp;
import javax.persistence.*;

public class Attachment {
    private Integer id;
    private Timestamp created_at;
    private Timestamp updated_at;    
    private String name;
    private String description;
    private String type;
    private Authority authority; 
    private File file; 
    private Content content; 
    private User user;                        

    public Integer getId () {
        return id;
    }

    public void setId (Integer id) {
        this.id = id;
    }

    public Timestamp getCreated_at() {
        return created_at;
    }

    public void setCreated_at(Timestamp created_at) {
        this.created_at = created_at;
    }

    public Timestamp getUpdated_at() {
        return updated_at;
    }

    public void setUpdated_at(Timestamp updated_at) {
        this.updated_at = updated_at;
    }

    public String getName () {
        return name;
    }

    public void setName (String name) {
        this.name = name;
    }    

    public String getType () {
        return type;
    }

    public void setType (String type) {
        this.type = type;
    } 

    public String getDescription () {
        return description;
    }

    public void setDescription (String description) {
        this.description = description;
    }

    public Authority getAuthority () {
        return authority;
    }

    public void setAuthority (Authority authority) {
        this.authority = authority;
    }    

    public File getFile () {
        return file;
    }

    public void setFile (File file) {
        this.file = file;
    }   

    public Content getContent () {
        return content;
    }

    public void setContent (Content content) {
        this.content = content;
    } 

    public User getUser () {
        return user;
    }

    public void setUser (User user) {
        this.user = user;
    }                                
}
/usr/local/apache-tomcat