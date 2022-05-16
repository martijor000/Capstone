using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using WebAPI.Models;

namespace WebAPI.Controllers
{
    public class HomeController : Controller
    {
        public ActionResult Index()
        {
            ViewBag.Title = "Home Page";
            return View();
        }
        public ActionResult CalculateList(Items model)
        {
            if (ModelState.IsValid)
            {
                AccessoryController accessoryController = new AccessoryController();
                List<BabyAccessory> allItems = new List<BabyAccessory>(accessoryController.Get().ToList());
                List<double?> comparePrice = new List<double?>();

                for (int j = 0; j < model.GroceryList.Count; j++) 
                {
                    for (int i = 0; i < allItems.Count; i++)
                    {
                        if (allItems[i].name.ToLower().Contains(model.GroceryList[j].ToString().ToLower()))
                        {
                            if (model.GroceryList[j] != "")
                            {
                                comparePrice.Add(allItems[i].price);   
                            }
                            else
                            {
                                continue;
                            }
                        }
                        else
                        {
                            Console.WriteLine("Nope not found");
                        }
                    }

                }
                comparePrices(comparePrice);
            }
            return RedirectToAction("Index", "CalculateIndex", model);
        }
        private void comparePrices(List<double?> compare)
        {
            if(compare != null)
            {
                for (int i = 0; i < compare.Count; i++)
                {
                    for(int j = 0; j < compare.Count; j++)
                    {
                        if (compare[i] > compare[j])
                        {
                            Console.WriteLine(compare[i]);
                        }
                    }
                }
            }
        }
        private void returnInputs(List<Items> saveList)
        {

        }
    }
}
