using System;
using System.Collections.Generic;
using System.Linq;
using System.Web;
using System.Web.Mvc;
using WebAPI.Models;

namespace WebAPI.Controllers
{
    public class CalculateIndexController : Controller
    {
        // GET: CalculateIndex
        public ActionResult Index()
        {
            return View();
        }
    }
}