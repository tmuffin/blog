/**
 * Created by Philip 
 */

package com.blog.entity;

import java.sql.Timestamp;
import javax.persistence.*;

public class RoleAuthority {
    private Integer id;

    private Integer roleId;
    private Integer authorityId;

    private Timestamp created_at;
    private Timestamp updated_at;
    
    /**
     * 获取模型id
     * @return {Integer} 模型id
     */
    public Integer getId () {
        return id;
    }

    /**
     * 设置id
     * @param {Integer} id 
     * @return none
     */
    public void setId (Integer id) {
        this.id = id;
    }

    public Timestamp getCreated_at() {
        return created_at;
    }

    public void setCreated_at (Timestamp created_at) {
        this.created_at = created_at;
    }

    public Timestamp getUpdated_at () {
        return updated_at;
    }

    public void setUpdated_at (Timestamp updated_at) {
        this.updated_at = updated_at;
    }

    public Integer getRoleId () {
        return roleId;
    }

    public void setRoleId (Integer roleId) {
        this.roleId = roleId;
    }    

    public Integer getAuthorityId () {
        return authorityId;
    }

    public void setAuthorityId (Integer description) {
        this.authorityId = authorityId;
    }
}
