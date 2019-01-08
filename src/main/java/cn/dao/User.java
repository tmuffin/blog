/**
 * DAO: 用户
 * @author Philip
 */
package cn.muffino.dao;

import cn.muffino.model.User;

public interface UserDao {
	public User selectUserById(Integer userId);  
}
