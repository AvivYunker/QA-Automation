using System;
using OpenQA.Selenium;
using OpenQA.Selenium.Chrome;
using System.Threading;
class SauceLabsTest
{
    static void Main()
    {
        IWebDriver browser = new ChromeDriver();

        browser.Navigate().GoToUrl("https://techstepacademy.com/trial-of-the-stones");

        IWebElement riddleOfStoneTextField = browser.FindElement(By.Id("r1Input"));
        IWebElement answerButton1 = browser.FindElement(By.Id("r1Btn"));
        
        riddleOfStoneTextField.SendKeys("rock");
        answerButton1.Click();
        IWebElement answer1 = browser.FindElement(By.XPath(@"//*[@id='passwordBanner']/h4"));
        string answer1String = answer1.Text;

        IWebElement riddleOfSecretsTextField = browser.FindElement(By.Id("r2Input"));
        IWebElement answerButton2 = browser.FindElement(By.Id("r2Butn"));
        riddleOfSecretsTextField.SendKeys(answer1String);
        answerButton2.Click();
        IWebElement answer2 = browser.FindElement(By.XPath(@"//*[@id='successBanner1']/h4"));
        string answer2String = answer2.Text;

        IWebElement merchant1Name = browser.FindElement(By.XPath(@"//*[@id='block-05ea3afedc551e378bdc']/div/div[3]/span/b"));
        IWebElement merchant1Wealth = browser.FindElement(By.XPath("//*[@id='block-05ea3afedc551e378bdc']/div/div[3]/p"));
        IWebElement merchant2Name = browser.FindElement(By.XPath(@"//*[@id='block-05ea3afedc551e378bdc']/div/div[4]/span/b"));
        IWebElement merchant2Wealth = browser.FindElement(By.XPath(@"//*[@id='block-05ea3afedc551e378bdc']/div/div[4]/p"));
        IWebElement richestMerchantAnswer = browser.FindElement(By.Id("r3Input"));
        IWebElement answerButton3 = browser.FindElement(By.Id("r3Butn"));

        string merchant1NameString = merchant1Name.Text;
        int merchant1WealthInt = int.Parse(merchant1Wealth.Text);
        string merchant2NameString = merchant2Name.Text;
        int merchant2WealthInt = int.Parse(merchant2Wealth.Text);

        string richestMerchant = "";
        if (merchant1WealthInt > merchant2WealthInt)
        {
            richestMerchant = merchant1NameString;
        }
        else if (merchant1WealthInt < merchant2WealthInt)
        {
            richestMerchant = merchant2NameString;
        }
        else
        {
            richestMerchant = "none";
        }
        richestMerchantAnswer.SendKeys(richestMerchant);
        answerButton3.Click();

        IWebElement checkAnswersButton = browser.FindElement(By.Id("checkButn"));
        checkAnswersButton.Click();
        IWebElement finalResults = browser.FindElement(By.XPath(@"//*[@id='successBanner2']/h4"));
        string finalResultsString = finalResults.Text;

        if (finalResultsString.Equals("Success!"))
        {
            Console.WriteLine("\nV\n");
        }
        else
        {
            Console.WriteLine("\nX\n");
        }
        Console.WriteLine("The final text was: " + finalResultsString);
    }
}