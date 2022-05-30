using System;
using System.Collections.Generic;
using System.Drawing;
using System.Linq;
using System.Web.Mvc;
using System.Windows.Forms;
using TypeNSaveWebForm.Controllers.SafewayControllers.Baby;
using TypeNSaveWebForm.Models.Safeway.Baby;
using TypeNSaveWebForm.Models.Universal;

namespace TypeNSaveWebForm.Controllers
{
    public class HomeController : Controller
    {
        private List<double?> comparePrice = new List<double?>();
        private static AccessoryController accessoryController = new AccessoryController();
        private List<BabyAccessory> allItems = new List<BabyAccessory>(accessoryController.Get().ToList());
        private List<string> temp = new List<string>();
        private List<string> duplicateItems = new List<string>();
        private List<double?> returnPrice = new List<double?>();
        private List<string> returnItems = new List<string>();
        private ModelViewIndex modelViewIndex = new ModelViewIndex();
        

        public ActionResult Index()
        {
            ModelViewIndexSizes();
            modelViewIndex.ItemsModel.ItemName = new List<string> { "", "", "", "", "" };
            ViewBag.Title = "Home Page";
            return View(modelViewIndex);
        }

        public void ModelViewIndexSizes()
        {
            modelViewIndex.ItemsModel = new Items();
            foreach (var item in allItems)
            {
                temp.Add(item.unitOfMeasure);
            }
            modelViewIndex.Sizes = temp.Distinct().ToList();
        }

        public ActionResult MyButtonAction(string buttonClicked, Items model)
        {
            switch (buttonClicked)
            {
                case "Calculate":
                    return (CalculateList(model));
                case "Add Another Item":
                    return (AddItem(model));
                case "Clear":
                    return (ClearIndex());
                default:
                    return (View(Index()));
            }
        }

        public ActionResult CalculateList(Items model)
        {
            if (ModelState.IsValid)
            {
                foreach (string listItem in model.ItemName)
                {
                    DatabaseLoop(listItem);
                }
                comparePrices(comparePrice);
                TempData["GrabItemProducts"] = returnItems;
                TempData["GrabItemPrices"] = returnPrice;
            }
            return RedirectToAction("Index" , "CalculateIndex");
        }

        private void DatabaseLoop(string itemName)
        {
            for (int i = 0; i <  allItems.Count; i++)
            {
                if (allItems[i].name.ToLower().Contains(itemName.ToLower()))
                {
                    if (itemName != "")
                    {
                        duplicateItems.Add(allItems[i].name);
                        comparePrice.Add(allItems[i].price);
                    }
                    else
                    {
                        break;
                    }
                }
            }
            
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
                            returnPrice.Add(compare[i]);
                            returnItems.Add(duplicateItems[i]);
                        }
                    }
                }
            }
        }
        public ActionResult AddItem(Items model)
        {
            ModelViewIndexSizes();
            model.ItemName.Add("");
            modelViewIndex.ItemsModel = model;
            return View("Index", modelViewIndex);
        }
        public ActionResult ClearIndex()
        {
            ModelState.Clear();
            return (Index());
        }
    }
}