using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System.Threading;
class CssSelectorExample
{
    static void Main()
    {
        IWebDriver browser = new ChromeDriver();
        IAlert alert;

        browser.Navigate().GoToUrl("https://techstepacademy.com/training-ground");

        // elements
        IWebElement textInputField1 = browser.FindElement(By.Name("Input 1"));
        IWebElement textInputField2 = browser.FindElement(By.Name("Input 2"));
        IWebElement button1 = browser.FindElement(By.Name("butn1"));
        IWebElement button2 = browser.FindElement(By.Name("butn2"));
        IWebElement button3 = browser.FindElement(By.Name("butn3"));
        IWebElement button4 = browser.FindElement(By.Name("butn4"));

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