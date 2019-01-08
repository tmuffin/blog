/**
 * 控制器: 角色
 * @author Philip
 */
package cn.muffino.controller;

import javax.annotation.Resource;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import cn.model.Role;
import cn.service.RoleController;

@Controller
public class RoleController {
  @Resource  
  private UserService userService;  

  @RequestMapping("/showUserInfo")    
  public ModelAndView getIndex () {      
    ModelAndView mav = new ModelAndView("index");
    User user = userService.selectUserById(1);

    mav.addObject("user", user);
    return mav;
  } 
}