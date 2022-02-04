using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System.Threading;
class IdSelectorExample
{
    static void Main()
    {
        IWebDriver browser = new ChromeDriver();
        IAlert alert;

        browser.Navigate().GoToUrl("https://techstepacademy.com/training-ground");

        // elements
        IWebElement textInputField1 = browser.FindElement(By.Id("ipt1"));
        IWebElement textInputField2 = browser.FindElement(By.Id("ipt2"));
        IWebElement button1 = browser.FindElement(By.Id("b1"));
        IWebElement button2 = browser.FindElement(By.Id("b2"));
        IWebElement button3 = browser.FindElement(By.Id("b3"));
        IWebElement button4 = browser.FindElement(By.Id("b4"));

        // actions
        textInputField1.SendKeys("sample text...");

        button1.Click();
        alert = browser.SwitchTo().Alert();
        alert.Accept();

        button2.Click();
        alert = browser.SwitchTo().Alert();
        alert.Accept();

        textInputField2.SendKeys("sample text...");

        button3.Click();
        alert = browser.SwitchTo().Alert();
        alert.Accept();

        button4.Click();
        alert = browser.SwitchTo().Alert();
        alert.Accept();

        Thread.Sleep(3000);

        browser.Quit();
    }
}