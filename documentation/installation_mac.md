# Installation Mac

Before you can use the framework please follow the installation instructions in chronological order:

## Global frameworks needed before installing Appium tools or Mobile platforms

### Install JDK and Set JAVA_HOME

- Download OpenJDK latest stable version (JDK17) for mac https://jdk.java.net/17/
  Go the download folder via your terminal
  ``` cd ~/Downloads ```
- Extract the .TAR file
  ``` tar xf openjdk-17_osx-x64_bin.tar.gz ```
- Copy the extracted folder to the following standard location on mac OS via this terminal command
  ``` sudo mv jdk-17.jdk /Library/Java/JavaVirtualMachines/ ```
- Set path to JAVA_HOME via
  ``` nano ~/.zshrc ```

Enter the path to JAVA_HOME and set the path to the bin folder

- export JAVA_HOME="/Library/Java/JavaVirtualMachines/jdk-17.jdk/Contents/Home"
- export PATH=$JAVA_HOME/bin:$PATH

### Install NVM - Node version manager

Node Version Manager Github(https://github.com/nvm-sh/nvm)

Check via the following command of NVM is part of the path

``` nano ~/.zshrc ```

It should look like this:

***export HOME="/Users/username"
export NVM_DIR="/Users/username/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"***

### Install latest stable release Node.js via NVM

``` nvm install --lts ```

Set latest stable Node LTS release as your default NodeJS version

``` nvm alias default node ```

Check whether the configuration is as expected with the following command

``` nvm current ```

This should output for example: **18.12.0**

### Appium tools

- [Appium Inspector](https://github.com/appium/appium-inspector) A GUI inspector for mobile apps
- [Install and Setup of Appium Server](https://dpgraham.github.io/appium-docs/setup/running-on-windows/) ``` npm install -g appium ```
- [Appium Doctor](https://github.com/appium/appium/tree/master/packages/doctor) ``` npm install  @appium/doctor -g ```
  Attempts to diagnose and fix common Node, iOS and Android configuration issues before starting Appium

#### Appium server requirements

To install appium server please look at the following [requirements](https://appium.io/docs/en/2.0/intro/requirements/).

#### Appium Inspector

In order to check different aspects of the mobile application we can use the Appium Inspector.

#### Setup Android emulators for Appium Inspector

In Android Studio you can set up emulators, for the demo it is recommended to have at least the following:

- Phone with the latest Android version
- Tablet with the latest Android version

To check the names of your emulators you can run the following command in the terminal:

``` emulator -list-avds ```

##### desired capabilities Android emulator

````
{
  "platformName": "android",
  "appium:automationName": "UiAutomator2",
  "appium:udid": "emulator-5554",
  "appium:app": "/absolute_path_to/testapps/proverbial_android.apk"
}
````

#### Setup Apple emulators for Appium Inspector

In Xcode, you can create specific emulators, for the demo it is recommended to have at least the following:

* Iphone SE with latest IOS version
* Ipad Air with the latest IOS version

To check the names of your emulators you can run the following command in the terminal:

``` instruments -s devices ```

##### desired capabilities IOS emulator

````
{
  "platformName": "iOS",
  "appium:automationName": "XCUITest",
  "appium:udid": "",
  "appium:app": "/absolute_path_to/testapps/proverbial_ios.ipa"
}
````

### ANDROID

#### Install Android Studio with the SDK

- Download and install [Android Studio](https://developer.android.com/studio)
- Set paths to ANDROID_HOME and others via the command:  ``` nano ~/.zshrc ```

Set the following paths in your ZSH profile

- export ANDROID_HOME="/Users/{replace your userprofile name}/Library/Android/sdk"
- export PATH=$ANDROID_HOME/tools:$PATH
- export PATH=$ANDROID_HOME/platform-tools:$PATH
- export PATH=$ANDROID_HOME/build-tools:$PATH
- export PATH=$ANDROID_HOME/emulator:$PATH
- export PATH=$ANDROID_HOME/tools/bin:$PATH

### IOS

#### Install XCode

- Download and install XCode via the AppStore
- Install XCode Command Line Tools
- Install NVM - Node version manager
- Install latest stable release NodeJS via NVM
- Install [brew package manager](https://brew.sh/index_nl)
- Install Carthage via command ``` brew install carthage ```
- After installation carthage please execute the following command ```xcode-select```
- ```sudo xcode-select -s /Applications/Xcode.app/Contents/Developer```

