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
        private static AccessoryController accessoryController = new AccessoryController();
        private ModelViewIndex modelViewIndex = new ModelViewIndex();
        private List<BabyAccessory> allItems = new List<BabyAccessory>(accessoryController.Get().ToList());

        private List<double?> returnPrice = new List<double?>();
        private List<double?> returnSinglePrice = new List<double?>();
        private List<string> returnItems = new List<string>();
        private List <int> itemIndex = new List<int>();
        private List<int> amtIndex = new List<int>();


        public ActionResult Index()
        {
            ModelViewIndexSizes();
            modelViewIndex.ItemsModel.ItemName = new List<string> { "", "", "", "", "" };
            modelViewIndex.ItemsModel.ItemAmount = new List<int> {1, 1, 1, 1, 1 };
            ViewBag.Title = "Home Page";
            return View(modelViewIndex);
        }

        public void ModelViewIndexSizes()
        {
            modelViewIndex.ItemsModel = new Items();
            modelViewIndex.Sizes = new List<string>();
            foreach (var item in allItems)
            {
                modelViewIndex.Sizes.Add(item.unitOfMeasure);
            }
            modelViewIndex.Sizes = modelViewIndex.Sizes.Distinct().ToList();

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

                if (DatabaseLoop(model))
                {
                    comparePrices(itemIndex, model);
                    StoreTempData(model);
                }
                
                TempData["GrabItemProducts"] = returnItems;
                TempData["GrabItemPrices"] = returnPrice;
                TempData["GrabSinglePrices"] = returnSinglePrice;
            }
            return RedirectToAction("Index" , "CalculateIndex");
        }

        private bool DatabaseLoop(Items model)
        {
            for (int i = 0; i < model.ItemName.Count; i++)
            {
                if (model.ItemName[i] != "")
                {
                    for (int j = 0; j < allItems.Count; j++)
                    {
                        if (allItems[j].name.ToLower().Contains(model.ItemName[i].ToLower()))
                        {
                            itemIndex.Add(j);
                        }
                    }
                }
            }
            
            if(itemIndex.Count != 0)
            {
                return true;
            }
            else
            {
                return false;
            }

        }
        private void comparePrices(List<int> ind, Items model)
        {
            if (ind != null)
            {
                for (int i = 0; i < ind.Count; i++)
                {
                    for (int j = 0; j < ind.Count; j++)
                    {
                        if (allItems[ind[i]].price < allItems[ind[j]].price)
                        {
                            amtType(allItems[ind[i]].unitOfMeasure, allItems[ind[i]].name, allItems[ind[i]].price, allItems[ind[i]].pricePer);

                            break;
                        }
                    }
                }
            }
        }

        private void amtType(string type, string name, double? price, double? pricePer)
        {
            returnItems.Add(name);

                switch (type)
                {
                    case "CT":
                        returnSinglePrice.Add(price);
                        break;
                    case "LB":
                        returnSinglePrice.Add(pricePer);
                        break;
                    case "OZ":
                        returnSinglePrice.Add(pricePer);
                        break;
                    case "EA":
                        returnSinglePrice.Add(price);
                        break;
                    case "PT":
                        returnSinglePrice.Add(pricePer);
                        break;
                }
        }

        private void StoreTempData(Items model)
        {
            for (int i = 0; i < model.ItemName.Count; i++)
            {
                if(model.ItemName[i] != "")
                {
                    returnPrice.Add(returnSinglePrice[i] * model.ItemAmount[i]);
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
            return RedirectToAction("Index");
        }
    }
}