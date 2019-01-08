/**
 * Model: 日记
 * @author Philip
 */
package cn.muffino.model;

public class Journal {
  private Integer userId;  
  private String userName;  
  private String userPassword;  

  public Integer getUserId() {  
    return userId;  
  }  

  public void setUserId(Integer userId) {  
    this.userId = userId;  
  }  

  public String getUserName() {  
    return userName;  
  }  

  public void setUserName(String userName) {  
    this.userName = userName;  
  }  

  public String getUserPassword() {  
    return userPassword;  
  }  

  public void setUserPassword(String userPassword) {  
    this.userPassword = userPassword;  
  } 
}
