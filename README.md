# Example Graph RAG

## Overview

This repository provides an example implementation of the Graph RAG (Graph-based RAG) pipeline described in the [paper](https://arxiv.org/abs/2404.16130) "From Local to Global: A Graph RAG Approach to Query-Focused Summarization" by Darren Edge et al. The implementation is written in Python and demonstrates how to process documents, build a graph, detect communities, and generate a final answer to a query.

## Prerequisites

Create a `.env` file in the root of the project with the following variables:

```bash
OPENAI_API_KEY=YOUR_OPENAI_API_KEY
```

- Python 3.12 or later
  - After installing Python, use pip to install the following packages:
    - `pip install openai networkx leidenalg cdlib python-igraph python-dotenv`

```
conda install pip

pip install -r requirements.txt
```    

## Implementation

The following steps are implemented in the `app.py` file, in accordance with the paper's description:

### 1. Source Documents → Text Chunks

- **Paper:** Describes splitting input texts into chunks for processing.
- **Code:** `split_documents_into_chunks` function splits the documents into chunks of a specified size with overlap.

### 2. Text Chunks → Element Instances

- **Paper:** Describes extracting entities and relationships using an LLM.
- **Code:** `extract_elements_from_chunks` function uses OpenAI's GPT-4 to extract entities and relationships from each chunk of text.

### 3. Element Instances → Element Summaries

- **Paper:** Describes summarizing extracted elements into meaningful summaries.
- **Code:** `summarize_elements` function uses GPT-4 to summarize the entities and relationships.

### 4. Element Summaries → Graph Communities

- **Paper:** Describes building a graph from element summaries and using community detection algorithms.
- **Code:** `build_graph_from_summaries` function creates a graph with nodes and edges based on the summaries. `detect_communities` function uses the Leiden algorithm to detect communities in the graph.

### 5. Graph Communities → Community Summaries

- **Paper:** Describes summarizing each detected community.
- **Code:** `summarize_communities` function concatenates the elements of each community into a summary.

### 6. Community Summaries → Community Answers → Global Answer

- **Paper:** Describes generating answers from community summaries and combining them into a final answer.
- **Code:** `generate_answers_from_communities` function generates intermediate answers based on community summaries and combines them into a final answer using GPT-4.

### Putting It All Together

- **Paper:** Describes a full pipeline that processes the documents, builds a graph, detects communities, and generates a final answer to a query.
- **Code:** `graph_rag_pipeline` function implements the full pipeline as described.

### Example Usage

- **Code:** The provided example demonstrates how to use the pipeline to process documents and generate an answer to a query, which aligns with the paper's goal of answering global questions over a text corpus.

To run the example once the dependencies have been installed, use the following command:

```bash
python app.py
```

Example query:

```
What are the main themes in these documents?
```

Example Graph RAG output:

```
 The main themes in these documents span across several domains, highlighting their interconnections and broader implications:

1. **Renewable Energy**:
    - **Types of Power Generation**: Focus on hydropower, geothermal, and solar energy as key renewable sources.
    - **Energy Security and Efficiency**: Emphasis on the role of renewable energy in improving energy security and promoting efficiency.
    - **Technological Advancements**: Improvements in technologies such as solar panels, energy storage solutions, and geothermal efficiency.
    - **Environmental Impact Management**: Strategies for minimizing the ecological footprint of renewable energy projects.

2. **Climate Change and Agriculture**:
    - **Impact on Agriculture**: Effects on crop yields, livestock, and the need for climate-resilient practices.
    - **Adaptation Strategies**: Development of new farming techniques, water management, and sustainable soil management to cope with changing climates.
    - **Food Security**: Addressing the combined impacts of climate change on agricultural productivity and food availability.

3. **Environmental Policies and International Cooperation**:
    - **Regulations and Agreements**: Implementation of policies like the Paris Agreement and Convention on Biological Diversity to conserve resources and reduce pollution.
    - **Sustainable Resource Management**: Focus on conserving water, reducing hazardous chemicals, and mitigating biodiversity loss.
    - **Global Efforts**: Coordinated international actions to tackle environmental challenges.

4. **Water Management**:
    - **Supply and Distribution**: Efficient allocation of water resources among various sectors.
    - **Irrigation and Agriculture**: The role of irrigation in supporting agricultural practices.
    - **Clean Water Access**: Ensuring safe water for human health, agricultural, and ecosystem sustainability.
    - **Environmental Concerns**: Addressing water scarcity, pollution, wastewater treatment, and conservation of aquatic ecosystems.

5. **Technological and Economic Impacts**:
    - **Supply Chain Disruptions**: Economic effects on agriculture and the need for resilient systems.
    - **Innovation in Agriculture**: Adopting new technologies to enhance productivity.
    - **Economic Sustainability**: Balancing environmental sustainability with economic growth in the agricultural sector.

These themes collectively underscore the importance of sustainability, technological advancement, resilient agricultural practices, effective policies, and international cooperation in addressing the interconnected challenges of energy, climate change, and environmental conservation.

```

_Note that the example uses a multiple albeit small documents for simplicity. In a real-world scenario, you would need to process multiple large documents and answer multiple queries. Expect the script to run for several minutes and cost around $3-5 in OpenAI credits using the GPT-4o model for all of the NLP tasks._
````
