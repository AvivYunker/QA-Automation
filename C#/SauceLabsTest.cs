using System;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System.Threading;
class SauceLabsTest
{
    static void Main()
    {
        IWebDriver browser = new ChromeDriver();

        browser.Navigate().GoToUrl("https://www.saucedemo.com/");

        // PAGE 1 (elements)
        IWebElement userNameTextField = browser.FindElement(By.Id("user-name"));
        IWebElement passwordTextField = browser.FindElement(By.Id("password"));
        IWebElement loginButton = browser.FindElement(By.Id("login-button"));

        // PAGE 1 (actions)
        userNameTextField.SendKeys("standard_user");
        passwordTextField.SendKeys("secret_sauce");
        loginButton.Click();

        // PAGE 2 (elements)
        IWebElement sauceLabsBackpackAddToCartButton = browser.FindElement(By.Id("add-to-cart-sauce-labs-backpack"));
        IWebElement sauceLabsBikeLightAddToCartButton = browser.FindElement(By.Id("add-to-cart-sauce-labs-bike-light"));
        IWebElement sauceLabsBoltTShirtAddToCartButton = browser.FindElement(By.Id("add-to-cart-sauce-labs-bolt-t-shirt"));
        IWebElement sauceLabsFleeceJacketAddToCartButton = browser.FindElement(By.Id("add-to-cart-sauce-labs-fleece-jacket"));
        IWebElement sauceLabsOnesieAddToCartButton = browser.FindElement(By.Id("add-to-cart-sauce-labs-onesie"));
        IWebElement sauceLabsRedTShirtAddToCartButton = browser.FindElement(By.Id("add-to-cart-test.allthethings()-t-shirt-(red)"));
        IWebElement shoppingCartButton = browser.FindElement(By.ClassName("shopping_cart_link"));

        // PAGE 2 (actions)
        sauceLabsBackpackAddToCartButton.Click();
        sauceLabsBikeLightAddToCartButton.Click();
        sauceLabsBoltTShirtAddToCartButton.Click();
        sauceLabsFleeceJacketAddToCartButton.Click();
        sauceLabsOnesieAddToCartButton.Click();
        sauceLabsRedTShirtAddToCartButton.Click();
        shoppingCartButton.Click();

        // PAGE 3 (elements)
        IWebElement checkOutButton = browser.FindElement(By.Id("checkout"));

        // PAGE 3 (actions)
        checkOutButton.Click();

        // PAGE 4 (elements)
        IWebElement firstNameTextField = browser.FindElement(By.Id("first-name"));
        IWebElement lastNameTextField = browser.FindElement(By.Id("last-name"));
        IWebElement postalCodeTextField = browser.FindElement(By.Id("postal-code"));
        IWebElement continueButton = browser.FindElement(By.Id("continue"));

        // PAGE 4 (actions)
        firstNameTextField.SendKeys("first");
        lastNameTextField.SendKeys("last");
        postalCodeTextField.SendKeys("12345");
        continueButton.Click();

        // PAGE 5 (elements)
        //Thread.Sleep(8000);
        IWebElement finishButton = browser.FindElement(By.Id("finish"));

        // PAGE 5 (actions)
        finishButton.Click();

        // PAGE 6 (elements)
        IWebElement successMessage = browser.FindElement(By.CssSelector("#checkout_complete_container > h2"));
        string successMessageString = successMessage.Text;

        if (successMessageString == "THANK YOU FOR YOUR ORDER")
        {
            Console.WriteLine("\nV\n");
        } else
        {
            Console.WriteLine("\nX\n");
        }
        Console.WriteLine("The message was: " + successMessageString);
    }
}