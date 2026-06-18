# **ARSSDC Bellevistat Project**

Welcome to the repository for my ARSSDC (Asian Regional Space Settlement Design Competition) Bellevistat project. This record contains the designs, structural layouts, and operational plans for our proposed Earth-orbit space settlement and industrial manufacturing hub (basically the final submitted doc).

## **The Habitability & Artificial Gravity Simulator**

To back up our structural designs and demonstrate the physics of our settlement, this repository also includes a Python script: bellevistat\_analysis.py.

Designing a rotating space settlement isn't just about hitting exactly 1G; it requires balancing several physiological constraints outlined in the NASA 1975 Summer Study. This script acts as an interactive calculator and data visualizer to map out those constraints:

* **Artificial Gravity & Coriolis Limits:** Calculates the relationship between station radius, rotation rate (RPM), and simulated gravity. It automatically warns if the rotation exceeds 4 RPM (the threshold for severe Coriolis motion sickness).  
* **Gravity Gradients:** Models the head-to-foot gravity variance to ensure blood flow isn't disrupted (must be kept under 15%).  
* **Agricultural Footprint:** Calculates the required square footage for hydroponic/aeroponic food production based on the expected population size.  
* **Advanced Dashboard:** Generates a comprehensive, dark-themed matplotlib visualization of the "Habitability Parameter Space," proving our dimensions hit the scientific "Sweet Spot."

**How to run it:**

Ensure you have numpy and matplotlib installed, then run:

python bellevistat\_analysis.py

### **A Note to Future Participants**

If you are reading this and looking to get into ARSSDC yourself, here is a quick piece of advice: **for the first round, the emphasis is heavily on the freshness of your ideas.**

It might seem completely daunting at first, but I promise you it is definitely doable. To give you some context, our team procrastinated for about three weeks and ended up grinding out this entire project in just five days—and we still made it\!

Don't paralyze yourself by overthinking the extreme technical complexities. Just try to imagine unique solutions and present whatever you come up with in a realistic, explainable setting. It is not expected that you will create some revolutionary scientific discovery. You are absolutely free to try and highly encouraged to do so, but it is not the most important thing to pass the first stage.

Focus on creativity, make sure your concepts can be logically explained, try not to repeat our procrastination streak, and have fun building your settlement.
