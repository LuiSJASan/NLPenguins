import math
import re
from collections import Counter

def tokenize(text):
    # Split text into paragraphs by two new line characters
    paragraphs = text.split('\n\n')
    
    # Further split paragraphs into words, remove punctuation, and convert to lowercase
    tokens = [re.findall(r'\b\w+\b', paragraph.lower()) for paragraph in paragraphs]
    
    return tokens

def calculate_shannon_entropy(paragraph):
    # Calculate word frequencies
    word_counts = Counter(paragraph)
    total_words = len(paragraph)
    
    # Calculate probabilities and entropy
    entropy = -sum((count/total_words) * math.log2(count/total_words) for count in word_counts.values())
    
    return entropy

def calculate_word_count(paragraph):
    return len(paragraph)

def score_paragraphs(paragraphs, alpha=0.5, beta=0.5):
    scores = []
    entropies = [calculate_shannon_entropy(paragraph) for paragraph in paragraphs]
    word_counts = [calculate_word_count(paragraph) for paragraph in paragraphs]
    
    # Normalize metrics
    max_entropy = max(entropies) if max(entropies) > 0 else 1
    max_word_count = max(word_counts) if max(word_counts) > 0 else 1
    
    normalized_entropies = [entropy/max_entropy for entropy in entropies]
    normalized_word_counts = [word_count/max_word_count for word_count in word_counts]
    
    # Calculate scores and append first five words of each paragraph
    for entropy, word_count, paragraph in zip(normalized_entropies, normalized_word_counts, paragraphs):
        score = alpha * entropy + beta * (1 - word_count)
        first_five_words = ' '.join(paragraph[:5])
        if first_five_words == "":
            first_five_words ="{empty}"
        else:
            first_five_words += "..."
        scores.append((score, first_five_words))
    
    return scores

# Sample text with paragraphs separated by two new line characters
text = """
Recently, the global landscape of AI has begun to shift significantly. AI has become massively popular in the last year thanks to widely accessible tools like ChatGPT, revealing a significant shift in how technology intersects with our daily lives.
It’s another bustling Wednesday in your clinic, patients are waiting, and you’re juggling diagnoses, treatment plans and a lot of administrative tasks and you wonder if there is a way to reduce the hours spent on patient records and increase time for direct patient care. Artificial Intelligence (AI) might have the answer.

The concept of AI started more than 60 years ago, but only around 2005 it became more popular once the access to big data and prices for highly demand computing power was cheaper, allowing its use in practical applications in complex, real-world tasks.

In healthcare, in particular, AI still plays an important role, transforming the way we approach diagnostics by analyzing medical images like X-Rays, MRIs and CT scans. Important contributions also for drug discovery and development, predictive analytics, health monitoring, etc. However, until now, the use of AI was confined to specific fields and for certain tasks, not fully integrated into broader clinical practices.

AI has simply become extremely popular because it can be used in many different fields, including healthcare, and reshaping some areas previously untouched. This has opened up new possibilities that were unimaginable just a few years ago.

This new and particular brand of AI technology is what is known as Generative AI and it is very well suited for what it’s coming in healthcare for the next years.

## Generative AI

Generative AI it’s becoming real leapfrog for the human kind. Internet and mobile age were about putting information into the hands of everyone across the planet. They started out unevenly distributed, but not today. The AI age will be about putting intelligence into the hands of everyone across the planet. This transformative potential is what’s driving the massive investments by high-tech companies, envisioning a future where AI augments human potential, reshapes industries, and redefines the boundaries of innovation, specially in three sectors: Education, Coding and Healthcare.

_"In order to use the Force to your advantage, understand it first, you must.”_ - Yoda

Much like understanding the Force is crucial to harnessing its power, a bit of understanding on Generative AI is key to understand its potential. 

At its core, generative AI technology relies on two key elements: vast quantities of existing content and a sophisticated process that transforms this content into new, coherent pieces of text, video, and images. This foundational mechanism enables the AI to exhibit remarkable capabilities, such as producing original and contextually relevant content.

### The Dawn of a New Era

Our story begins on a notable date: November 30, 2022. This day marked the unveiling of Generative AI to the public, a leap forward anchored by OpenAI. Visionaries like Elon Musk and companies such as Microsoft backed this endeavor, aiming to redefine how machines understand and generate human language.

### Understanding the Architects: Large Language Models

At the heart of Generative AI are Large Language Models (LLMs), conceptualized by OpenAI. Picture these as colossal libraries, storing not books, but fragments of digital text from the expanse of the internet. These models learn much like a child does, at a much larger scale, predicting the next word in a sentence. For example, given “The sky is…”, the model would guess “blue”.  This seemingly simple learning process is actually the cornerstone of this new technology, proving that **when simple components are scaled, complexity and depth emerge**.
As Stephen Wolfram articulates, LLMs fundamental goal is to generate a “reasonable continuation” of any given text, a continuation that aligns with patterns observed across billions of web pages.

And what is really happening behind the scenes is that, at a very large scale, these models can recognize patterns in text, discern relationships between words, and understand the underlying meaning in vast areas of language. This emerged sophisticated understanding is most visible when responses are not only contextually appropriate, but also rich in detail, resembling human comprehension. This intrinsic capability to analyze and interpret language at multiple levels distinguished Generative AI as a powerful tool, transcending the realm of basic text prediction to engage in meaningful, context-aware communication.
 
### The Power of Generative AI

With such immense training corpus, Generative AI, exemplified by ChatGPT, understands and processes natural language, enabling advanced communication tailored to user needs, closely mimicking human conversation. 

But the capabilities of Generative AI are not limited to the production of coherent and context-appropriate texts. It is the adaptability and versatility of these models what makes it possible from writing emails to composing poetic verses, from coding software to offering medical advice. Generative AI is rapidly becoming an indispensable tool in many areas. 

In sectors like education, Generative AI promises personalized learning experiences, where content is tailored to individual learning styles and paces. In coding, it acts as a co-pilot, suggesting code improvements and even writing substantial portions of code, which speeds up  project development. In healthcare, beyond managing administrative tasks, it has the potential to support diagnostic processes and offer preliminary guidance, although always under the watchful eye and expert judgement of healthcare professionals.

Yet, the true essence of Generative AI’s power lies in its potential as a  collaborative tool. It’s not about replacing human creativity or decision-making but augmenting it, offering tools that enhance human capabilities, fill gaps in knowledge or skill, and open doors to new possibilities. 
As we approach this exciting new frontier, it is evident that Generative AI with its capacity to understand, create and innovate, is set to reshape the boundaries of what technology can accomplish.

### The Pursuit of Human-Level Reasoning

The quest for **human-level reasoning** through massive data training is also underpinned as an extension of “complex behaviors often emerge from simple components at a sufficient scale.” The analogy here is astounding: Human actions which are driven by basic needs, desires, and instincts, are fundamentally simple but they become complex through the prism of social, cultural, economic, religious, and historical contexts. This level of complexity cannot be fully captured by relying on a single set of training data or a singular technological approach. 

What Generative AI has really brought us is a glimpse of a world in which the line between human reasoning and artificial computation is blurred. However, we have yet not there yet. The intricate dance of emotions, ethics and consciousness still remains in an enigmatic frontier not just beyond our current technology but also beyond our philosophical understanding of intelligence and consciousness. 

As we venture further into this uncharted territory, the future of AI seduces us with endless possibilities and profound questions. Will AI transcend the realm of data to truly understand the human condition, or will it remain a sophisticated but distinct echo of our own condition? The pursuit of Generative AI is more than a technological endeavor; it’s a mirror reflecting our deepest aspirations and existential curiosities, a journey that invites us to explore the very essence of intelligence, whatever it means.

But let's put those philosophical thoughts aside and just appreciate the amazing  technology we have right here and now.

## The role of Generative AI in Healthcare

Beyond the wide range of applications of AI and Generative AI in healthcare, some of them are unavoidable and require urgent solutions to keep patient care at the expected level. 

### Ratio doctors/patients

The global trend of an aging population is well-documented and is becoming increasingly significant. The The United Nations’ World Social Report 2023 highlights this issue, emphasizing that people are living longer, with the number of individuals aged 65 and older projected to more than double, rising to 1.6 billion by 2050. This trend is not confined to a single region but is a worldwide phenomenon, affecting both developed and developing nations.

The World Social Report 2023 emphasizes the need for specific and effective strategies to assist the increasingly aging population worldwide, particularly in light of rising costs associated with pensions and healthcare.

This global trend of aging populations poses significant implications for societies and economies worldwide, calling for comprehensive and forward-thinking approaches to manage the challenges and capitalize on the opportunities that come with an aging society.

Without a doubt, these demographic shifts require a reevaluation of policies related to work, social protection, and healthcare to accommodate and support an aging population.

### Increased paperwork

In today’s healthcare landscape, the burden of administrative tasks on medical professionals is reaching unprecedented levels. Physicians and healthcare workers find themselves entangled in an ever-growing web of paperwork, from exhaustive data entry to complex scheduling. This not only diverts their attention from patient care but also contributes to increased screen time, detracting from the invaluable face-to-face interaction with patients.

And this is where Generative AI comes in, a beacon of efficiency in this scenario. By automating repetitive and time-consuming tasks such as data entry, scheduling, and certain aspects of patient triage, Generative AI stands to revolutionize the administrative framework of healthcare. 

Beyond enhancing productivity, the integration of Generative AI into healthcare workflows promises collateral benefits. By liberating healthcare professionals from time-consuming tasks, we not only allow them to concentrate on crucial aspects of patient care but also substantially reduce their screen time. This shift in focus could lead to a marked improvement in both the quality of care and the overall patient experience.

Some hospitals are leading this technology, where traditional typewriting-while-listening method for recording patient histories is replaced by seamless digital audio recording. As the patient speaks, their words are not just recorded but transformed. Generative AI swiftly converts these conversations into precise, comprehensive clinical notes, perfectly tailored to the hospital's EMR system. The doctor's role evolves from scribe to reviewer, ensuring accuracy and completeness with a glance.

But the innovation doesn't stop at note-taking. Insurance paperwork is not a walk in the park. Generative AI navigates the intricate maze of policies, rules, forms, and procedures unique to each health insurance provider. From authorizations to referral notes, every document is meticulously filled out, drawing from the rich details of the patient's anamnesis.

And the patient's journey? It is transformed as well. As they step out of the clinic, they receive more than just a memory of the visit. Thanks to Generative AI, each patient is equipped with a clear, concise summary of their diagnosis and treatment plan, presented in language that is easy to understand, which increases the likelihood of engagement with treatment.

In summary, apart from increasing productivity, this will undoubtedly rebound in enhancing patient engagement and satisfaction.

### Curbside consultation

While the practice of physician-to-specialist consultations, often referred to as 'curbside consultation,' has a long-standing history, the introduction of Artificial Intelligence adds a new dimension by providing a supplementary, third opinion on diagnoses or treatment plans at any moment. Integrating AI into the medical recording systems ensures a seamless and efficient analysis of patient data that supports clinical decision-making process by doctors.

It’s like having a virtual consultant at your side, one that’s been trained on an extensive corpus of medical knowledge and continuously updated with the latest findings.

Think of this AI application as an evolution of search engines like Google or Bing, as it not only retrieves information, but also interprets and synthesizes it into cohesive, context-aware responses. Generative AI tools such as ChatGPT can understand and mimic human dialogue, providing more nuanced and conversational interactions. They can integrate diverse sources of information in real time, offering personalized and detailed explanations beyond the simple listing of search results. This represents a shift from passive information retrieval obtained from an Internet search to active participation in knowledge.

Moreover, AI’s ability to analyze extensive data and recognize intricate patterns introduces a new layer of insight. This could be pivotal in diagnosing complex cases where the synthesis of vast, varied information is crucial, potentially uncovering critical insights that might elude traditional analysis.

Two important notes here: 

 - It is crucial for implementers of this technology to guarantee it is grounded on a solid foundation of reputable research and literature, ensuring AI's responses are credible and reliable.

- this AI-assisted collaborator is designed to augment, not replace, the expertise of physicians and the invaluable tradition of physician-to-specialist consultations. The final decision-making authority always resides with the attending physician, with AI serving as a powerful tool to inform and illuminate the path to the best patient outcomes.”

In essence, this curbside consultation at any moment enrich the clinical decision-making process for doctors. 


## Conclusion

Historical trends suggest that technological advancements, particularly in the realm of AI, are unlikely to cease. Despite potential slowdowns due to increased and needed regulatory measures, the inherent power and potential of disruptive technologies like Generative AI will continue to attract significant investment from major tech companies.

Healthcare leaders and institutions must proactively adopt generative AI solutions to boost medical staff productivity and enhance patient experiences while ensuring robust internal governance around AI models. This forward movement will ensure an effective response to the evolving needs of our societies, including demographic changes such as the rising demand for care in an aging population and the challenges of doctor shortages.
"""

# Tokenize text and score paragraphs
paragraphs = tokenize(text)
scores = score_paragraphs(paragraphs)

# Display scores and first five words
for i, (score, first_five_words) in enumerate(scores):
    print(f"Paragraph {i+1} Score: {score:.3f}, First five words: \"{first_five_words}\"")
