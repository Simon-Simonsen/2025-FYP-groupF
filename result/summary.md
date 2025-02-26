# Projects in Data Science (2025)
Background of the problem      
When it comes to medical diagnosis, the role of image processing has been growing more and more for the last decades. MRI, CT and other image generating processes help us to explore the human body without doing any harm in it. Advanced image processing techniques assist in automating early detection, improving accuracy, and making dermatological care more accessible and efficient. What’s more, modern image processing has allowed us to diagnose illnesses based on simple pictures. Classifying skin lesions in this way can be very time efficient: patients do not have to spend time with going to the doctor, because an algorithm analyzes the pictures and draws conclusion. This solution can be highly beneficial for both the doctors and the patients. 

Dangers of misdiagnosis     
While automatizing skin lesion diagnosis has a lot of advantages, it also has a dangerous side. Errors of image processing can lead to misdiagnosis, which we have to take very seriously when it is about lethal conditions. Giving patients the wrong treatment or no treatment makes recovery harder, a lot of times it even makes the condition worse. It is a controversial question, whether the diagnosis of human doctors or trained algorithms is more punctual; combining both can be a good attempt to increase efficiency. 

Skin lesions and the diseases they cause   
A skin lesion is a part of the skin that has an abnormal growth or appearance compared with the skin around it. There are two categories of skin lesions: primary and secondary. Primary skin lesions are skin conditions present at birth or acquired over a person’s lifetime. Secondary skin lesions develop from irritated or manipulated skin lesions.  Skin lesions can be caused by various diseases, like infections, autoimmune disorders and cancer. Autoimmune diseases like psoriasis, lupus, and eczema also lead to chronic skin lesions. Some lesions, such as actinic keratosis, basal cell carcinoma, and melanoma, indicate skin cancer and require early detection. Allergic reactions, genetic disorders, and external factors can also contribute to skin damage. 

Why it’s important to recognize skin lesions at an early stage?    
Learning what to look for on your own skin gives you the power to detect cancer early, before it can become disfiguring or deadly. Early detection is especially important in conditions like melanoma, where survival rates are much higher when treated in the early stages. 

What we observe in the data:   
  Our first task was to annotate the pictures from 0 to 2 based on how much hair they contained. The reason for this is that hair can obscure the visibility of skin lesions, which makes it harder to segment lesion properly. So, we created an excel file with a column for every member of the group, and we categorized the pictures individually.  
The annotation for hair presence means:       
0 (None) - It is clear and easy to analyze the lesion area because the image has no visible hair   
1 (Some) - This might cause minor inference while observing the skin lesion   
2 (A lot) - The image has significant hair coverage, making it difficult to clearly see the lesion and observed it. In these cases, preprocessing (such as hair removal techniques) is often necessary before segmentation and classification.      
  Our second task was to write a code that remove hair from the skin lesion pictures to make the analysis easier. We used our image data loader to iterate over all the samples.  

Image668   
Before (left) and after (right): (Some hair removed but some still remain)   

Image671   
Before(left) and after(right): (more blurry, removing small black hair, but white hair remaining)  

Image759   
Before(left) and after(right): (removes black hair, but small white hair still stays)   

After running the code, we noticed that in some cases the results were different. The aim was to understand the reason for this, therefore we compared the segmented pictures to the original ones. We have found out that the code did not perform well on images with white hair, as the results were not visible regardless of the amount of hair present. When tested on images with a significant amount of dark hair, the code failed to remove all of it and, in some cases, caused distortions. The best results were achieved when the lesions had only a few dark hairs surrounding them. 

 








