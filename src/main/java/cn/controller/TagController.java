/**
 * 控制器: 标签
 * @author Philip
 */
package cn.muffino.controller;

import javax.annotation.Resource;

import org.springframework.stereotype.Controller;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.servlet.ModelAndView;

import cn.model.Tag;
import cn.service.TagService;

@Controller
public class MessageController {
  @Resource  
  private UserService userService;  

  @RequestMapping("/tag")    
  public ModelAndView getIndex () {      
    ModelAndView mav = new ModelAndView("index");
    User user = userService.selectUserById(1);

    mav.addObject("user", user);
    return mav;
  } 
}