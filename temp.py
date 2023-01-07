import torch
from transformers import pipeline

summarizer = pipeline(
    "summarization",
    "pszemraj/long-t5-tglobal-base-16384-book-summary",
    device=0 if torch.cuda.is_available() else -1,
)
long_text = """
Through the 1960s and into the ’70s, understanding human metabolism and fat storage became textbook science, even as the
authorities who were telling us how to eat healthy (focused on too much food causing obesity and too much dietary fat causing heart
disease) continued to find it of little interest. This understanding has mostly stayed textbook science. Go to your local medical library
or college bookstore (or bookshelf, if you’re a physician) and find a biochemistry textbook or an endocrinology textbook published
after, say, 1980. Look up fuel metabolism and insulin. In some textbooks, you might have to look under the word adipocyte—the
technical term for a fat cell—or adipose tissue. Then go to the pages specified, and that textbook will explain the hormonal regulation
of fuel metabolism, and since fuel storage is part of that process, it should explain what makes our fat cells store fat. It will do so in
technical terminology, but the message will be that insulin drives fat storage in the context of the elevated blood sugar that comes
with either eating a carb-rich meal or type 2 diabetes. *1 
Here’s the 2017 edition, for instance, of Lehninger Principles of Biochemistry, widely considered the most authoritative biochemistry
textbook, from the summary of a section on “Hormonal Regulation of Fuel Metabolism”: 
High blood glucose elicits the release of insulin, which speeds the uptake of glucose by tissues and favors the storage of fuels as
glycogen and triacylglycerols while inhibiting fatty acid mobilization in adipose tissue. 
Here’s a less technical translation: High blood sugar, which you can have when you either are diabetic or have eaten a carb-rich meal,
will prompt your pancreas to secrete insulin, which in turn will prompt you to burn the carbohydrates for fuel, store glucose as
glycogen and fat, and prompt your fat cells to store the fat you’ve eaten and the fat made from glucose and hold on to the fat it
already has. 
As a reminder of the power of paradigms and dogmatic thinking, the same textbook, on the very same page (939), says, “To a first
approximation obesity is the result of taking in more calories in the diet than are expended by the body’s fuel-consuming activities.”
The implication is that our fat cells get fat and fatter because our blood sugar goes up and insulin is elevated, but we get fat and
fatter because we eat too much. These are entirely different mechanisms, even though you’d think that we’d get fat and fatter for the
same reason our fat cells do. It is, after all, our fat cells that are getting fatter. 
I hesitate to use diagrams from human metabolism textbooks in a book meant to be readable for most anyone, but since this is
precisely what we want to know, I’m going to do it this one time. We want to know what regulates fat accumulations in fat cells, since,
as Bruch noted, when we’re overweight or obese, we’re dealing with excess fat accumulation in, well, fat cells. Here’s how this science
looks in a diagram from the 2019 edition of the textbook Metabolic Regulation in Humans, written by Keith Frayn of Oxford University
(with Rhys Evans). Before Frayn retired, a few years ago, he was considered among the two or three leading authorities in the world
on metabolism and particularly fat metabolism.￼ 
You can ignore the technical terminology in the diagram and pay attention to the bold arrows that I’ve added to the figure. As you can
see, everywhere the fat tissue is taking up fat, it’s insulin that’s promoting it—“Insulin +” as it’s labeled. When the fat tissue is
mobilizing fat, getting fat out of the cells and into the circulation where it can be used for fuel, it’s insulin that’s inhibiting it (“insulin
–”) and other hormones (adrenaline, noradrenaline, and ANP in the diagram) that are doing the promoting. (Frayn’s Metabolic
Regulation, too, goes on to blame human obesity on eating too much. The first time I interviewed Frayn, in February 2009, and
mentioned that he seemed to have two different mechanisms for excess fat accumulation in fat cells and excess fat accumulation in
humans, his immediate response, as I recall it, and I hope I’m not doing him a disservice, was that he had never considered that
before.) 
Metabolism researchers like to say that insulin is the signal for the “fed state,” meaning that it’s a signal that we’ve eaten, and we
have fuel available to store and use for energy. That actually oversimplifies the reality: Insulin is the signal that the body has been fed
carbohydrates. The fat we eat won’t stimulate insulin secretion. (While amino acids from protein are converted into glucose and
stimulate insulin secretion indirectly, the protein will also stimulate, as I said, glucagon and growth hormone secretion, so that signal
is far more nuanced.) When carbohydrates are consumed and insulin is secreted, it’s the carbohydrates that are used for energy, and
fat that is put in fat cells. So long as we keep eating carbohydrates and those carbohydrates are absorbed into the circulation, so long
as insulin remains elevated and the fat cells remain sensitive to that insulin, it will ensure that fat continues to be stored and to
accumulate. 
One obvious implication of this basic human physiology is that if we want to get fat out of our fat cells in any biologically efficient way,
we have to keep the insulin levels in our circulation low. We have to create that negative stimulus of insulin deficiency, which means
not eating carbohydrates. It’s all surprisingly simple if we work from the assumption—I would think a very reasonable one—that
human physiology, biochemistry, and endocrinology are actually relevant to a problem like obesity and why we get fat. The
authorities, for the past half century, have not done that. 

What’s both fascinating and dismaying about this history is that virtually everyone involved in the diet, weight-control, and health
business since the 1960s got at least something important wrong. This was one of the many factors that worked to make a simple
message appear to be complicated. Invariably these people made some assumptions based either on their preconceptions about
gluttony and sloth or on the role of dietary fat in heart disease. Some were simply enamored by the physics of thermodynamics and
couldn’t get away from the idea that what entered the body in excess, whatever that meant, had to be stored as fat. These biases led
them to make significant errors in how they interpreted all this evidence. 
It didn’t help that many of these “experts” had little meaningful scientific training. Typically they were medical doctors who got little
more mentoring in doing good science than do plumbers or any other talented artisans. Most of those who had been mentored inscience weren’t particularly good at it. They didn’t understand what it meant to be skeptical of their own ideas and so to check and
triple-check their assumptions. (“The first principle” of science, as the Nobel laureate physicist Richard Feynman put it so aptly, “is that
you must not fool yourself and you’re the easiest person to fool.”) As a result, these observations about the role of insulin, and the
implications that carbohydrates are fattening (specifically, to those who are predisposed to fatten easily), were never taken seriously
or considered relevant. They simply didn’t fit with the misconceived nutritional notions of the era. When they were taken into account,
invariably the researchers interpreted them simplistically and incorrectly. 
By 1965, for instance, as low-carb diets were becoming increasingly popular and the science to explain why they worked “as if by
magic” had been mostly elucidated, the nutritionists were already saying that the proclamations of physicians advocating for these
diets were either “nonsense” (no one can lose weight without eating less) or that the diets themselves were deadly (all that saturated
fat!), and that the public dissemination of this dietary guidance would result in “mass murder,” as Harvard’s Jean Mayer had suggested
to The New York Times in 1965. Mass murder! Mayer made that statement while clearly understanding the role of insulin in fat
accumulation—insulin “favors fat synthesis,” he wrote in his 1968 book Overweight, while speculating that different levels of insulin
and other hormones might have “different effects on the fat content of the body.” But Mayer couldn’t leave energy balance behind
and convinced himself that those who are fat ultimately get that way by being physically inactive. The passion for physical fitness that
Mayer helped promote began in the United States in the 1970s and is still going strong—coincident with ever-higher rates of obesity
and diabetes. 
The dietitians who were studying and reporting on the remarkable efficacy of LCHF/ketogenic eating—weight loss free from hunge
—seemed uninterested in discussing mechanisms that could explain this remarkable efficacy. If they paid attention to this science,
they rarely, if ever, talked or wrote about it publicly. Researchers who actually studied obesity would later latch on to the idea that the
fat we eat is the fat we store—as it mostly is—and this, coupled with the notion being widely promulgated that dietary fat caused
heart disease, led them to advise us to eat less fat (and replace it with carbohydrates) and that we’d prevent fat accumulation by
doing so. (This might even work in some people, but at a cost that might be exceedingly difficult to pay for a lifetime.) They never
made it to the next step in the process, which is that the carbohydrates we eat work to regulate, through insulin, that fat-storage
process and so how much of that dietary fat our fat cells will store and for how long. One influential researcher even floated a
hypothesis implying that the body so preferred storing fat to carbohydrates, thermodynamically, that if a food didn’t have fat in it,
then it couldn’t or wouldn’t make us fat. This led to the idea that even sugary beverages—free of fat, as they were—could be
consumed to our hearts’ content without influencing our waistlines. This was a disastrous misconception, but consumers in this
nutrition-obesity-chronic disease world had no protection from bad science and its ubiquitous misapplication. 
Even Robert Atkins, who came to fame in this era and knew that insulin was a fattening hormone, still argued in his massively best
selling diet book that his LCHF/ketogenic regimen worked so well because it stimulated some kind of “fat mobilizing hormone,” a
notion that had been proposed by British researchers in the 1950s and would never pan out. (The reality is that virtually all hormones,
with the notable exception of insulin, are technically fat-mobilizing hormones, although they won’t mobilize fat when insulin is
elevated. The insulin signal overrides that of these other hormones.) When a New York City physician and a Harvard-trained
nutritionist joined together to write and publish a scathing critique of Atkins’s diet book in 1974 under the imprimatur of the
American Medical Association, they pointed out that Atkins’s “fat-mobilizing hormone” was a canard and described Atkins’s diet as
based on “bizarre concepts of nutrition” that clearly shouldn’t be promoted to the general public. Then, as an aside to the fat
mobilizing hormone business, they noted that “fat is mobilized when insulin secretion diminishes.” That the Atkins diet, an LCHF
ketogenic diet, did among the better jobs imaginable of diminishing insulin secretion was not something the AMA thought should be
mentioned. *2 
*1 Even biochemistry and endocrinology textbooks tend to drift with the prevailing research fashions. Some simple “truisms” get left behind. In this
case, as medical science embraced first molecular biology, then genomics and proteomics and other disciplines made possible by the latest
technological innovations, even gut biomics, the study of the bacteria colonizing our GI tracts, textbooks have begun to omit some of this basic
science. 
*2 Hilde Bruch got it mostly right, but as I said, she wasn’t writing diet books. Here’s how she summarized this science in her 1973 book: “Fixation of
fatty acids in the adipose tissue for storage depends upon a continuous supply of glucose, and, inasmuch as insulin is required for utilization of this
glucose, it is obvious that control of fat metabolism is mediated by glucose and insulin....The implication of this interrelationship is that the excess
storage of fat as in obesity, might be associated with, or is the result of, an overproduction of insulin and excessive intake of carbohydrate food, or
both.” (Bruch 1973.) 
"""

result = summarizer(long_text)
print(result[0]["summary_text"])
