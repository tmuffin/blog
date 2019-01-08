/**
 * 控制器: 内容
 * @author Philip
 */
package cn.muffino.controller;

import javax.annotation.Resource;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import cn.model.Content;
import cn.service.ContentService;

@Controller
public class ContentController {
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