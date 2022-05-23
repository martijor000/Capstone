using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using TypeNSaveWebForm.Controllers.SafewayControllers.Baby;
using TypeNSaveWebForm.Models.Safeway.Baby;
using TypeNSaveWebForm.Models.Universal;

namespace TypeNSaveWebForm.Controllers
{
    public class HomeController : Controller
    {
        public ActionResult Index()
        {
            ViewBag.Title = "Home Page";
            return View();
        }

        [HttpPost]
        public ActionResult CalculateList(Items model)
        {
            Console.WriteLine(model.ItemName);
            if (ModelState.IsValid)
            {
                AccessoryController accessoryController = new AccessoryController();
                List<BabyAccessory> allItems = new List<BabyAccessory>(accessoryController.Get().ToList());
                List<double?> comparePrice = new List<double?>();

                for (int j = 0; j < model.ItemName.Count; j++)
                {
                    for (int i = 0; i < allItems.Count; i++)
                    {
                        if (allItems[i].name.ToLower().Contains(model.ItemName[j].ToString().ToLower()))
                        {
                            if (!string.IsNullOrEmpty(model.ItemName[j]))
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
                TempData["GrabItemModel"] = model;
            }
            return RedirectToAction("Index" , "CalculateIndex");
        }
        private void comparePrices(List<double?> compare)
        {
            if (compare != null)
            {
                for (int i = 0; i < compare.Count; i++)
                {
                    for (int j = 0; j < compare.Count; j++)
                    {
                        if (compare[i] < compare[j])
                        {
                            Console.WriteLine(compare[i]);
                        }
                    }
                }
            }
        }
    }
}