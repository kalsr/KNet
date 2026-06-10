import streamlit as st
import json
from io import BytesIO
import pandas as pd

# ------------------------------------------------------------------------------------
# CONFIG
# ------------------------------------------------------------------------------------
st.set_page_config(page_title="IOT Edge-Computing Taxonomy & Framework", layout="wide")

# ------------------------------------------------------------------------------------
# TOP TITLE BAR (BOLD BLUE)
# ------------------------------------------------------------------------------------
st.markdown(
    """
    <h1 style="color:#0047AB;"><b>IOT EDGE-COMPUTING TAXONOMY & FRAMEWORK APPLICATION</b></h1>
    <h3 style="color:#0047AB;"><b>Developed by Randy Singh, Kalsnt (KNet) Consulting Group</b></h3>
    """,
    unsafe_allow_html=True,
)

# ------------------------------------------------------------------------------------
# EXPLANATION: TAXONOMY VS FRAMEWORK IN EDGE COMPUTING
# ------------------------------------------------------------------------------------
st.markdown("### What is a Taxonomy in Edge Computing?")
st.write(
    "- **Taxonomy** is a structured classification system that organizes concepts, components, "
    "and use cases of edge computing into clear categories.\n"
    "- It helps you name, group, and compare things like functional roles (push from cloud, pull from IoT), "
    "use cases (cloud offloading, smart city), and challenges (privacy, programmability)."
)

st.markdown("### What is a Framework in Edge Computing?")
st.write(
    "- **Framework** is a practical structure or blueprint that shows **how** those classified elements "
    "work together in real systems.\n"
    "- It connects functions, use cases, and challenges into flows, architectures, and decision paths "
    "that can be implemented and evaluated."
)

st.markdown("### Difference and Benefits")
st.write(
    "- **Difference:** Taxonomy focuses on **classification and naming**; Framework focuses on **execution and structure**.\n"
    "- **Benefits of Taxonomy:** Common language, better communication, easier comparison of solutions.\n"
    "- **Benefits of Framework:** Repeatable design patterns, clearer decision-making, easier analysis of trade-offs, "
    "and better alignment between business goals and technical architecture."
)

st.markdown("---")

# ------------------------------------------------------------------------------------
# SIDEBAR – MAIN CATEGORY SELECTION
# ------------------------------------------------------------------------------------
st.sidebar.header("Edge-Computing Categories")
main_category = st.sidebar.radio(
    "Select Edge-Computing Category:",
    [
        "1. Functional Categories",
        "2. Use Cases",
        "3. Framework Challenges",
        "4. Taxonomy Matrix",
    ],
)

current_text_lines = []


def add_line(text: str):
    st.write(text)
    current_text_lines.append(text)


# ------------------------------------------------------------------------------------
# 6-TAB FRAMEWORK VIEW HELPER
# ------------------------------------------------------------------------------------
def framework_tabs():
    return st.tabs(
        [
            "Concept",
            "Flow",
            "Data Movement",
            "Control Plane",
            "Edge–Cloud Interaction",
            "Security View",
        ]
    )


# ------------------------------------------------------------------------------------
# FUNCTIONAL CATEGORIES
# ------------------------------------------------------------------------------------
if main_category.startswith("1"):
    st.markdown("## Functional Categories of IOT Edge-Computing")

    sub = st.selectbox(
        "Select Functional Subcategory:",
        [
            "1. Push from Cloud Services",
            "2. Pull from IoT",
            "3. Change from Data Consumer to Producer",
        ],
    )

    # ----------------- PUSH FROM CLOUD SERVICES -----------------
    if sub.startswith("1"):
        st.markdown("### Push from Cloud Services")
        add_line(
            "1. Putting all the computing tasks on the cloud has been proved to be an efficient way "
            "for data processing as the computing power on the cloud outclasses the capability of the "
            "things at the edge."
        )
        add_line(
            "2. Compared to the fast developing data processing speed, the bandwidth of the network "
            "has come to a standstill."
        )
        add_line(
            "3. Due to growing quantity of data generated at the edge, speed of data transportation "
            "is becoming the bottleneck for the cloud-based computing paradigm."
        )
        add_line(
            "4. If all the data needs to be sent to the cloud for processing, the response time would be too long."
        )
        add_line(
            "5. The data needs to be processed at the edge for shorter response time, more efficient processing "
            "and smaller network pressure."
        )

        concept_tab, flow_tab, data_tab, control_tab, interaction_tab, security_tab = framework_tabs()

        with concept_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    Cloud [shape=box, style=filled, color=lightblue];
                    Edge [shape=box, style=filled, color=lightgrey];
                    Things [shape=box, style=filled, color=lightyellow];

                    Cloud -> Edge [label="Tasks / data"];
                    Edge -> Things [label="Services"];
                    Things -> Edge [label="Telemetry"];
                    Edge -> Cloud [label="Aggregated data"];
                }
                """
            )

        with flow_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=TB;
                    step1 [label="1. Cloud generates tasks", shape=box];
                    step2 [label="2. Tasks pushed to Edge", shape=box];
                    step3 [label="3. Edge executes tasks near Things", shape=box];
                    step4 [label="4. Edge aggregates results", shape=box];
                    step5 [label="5. Edge sends summaries to Cloud", shape=box];

                    step1 -> step2 -> step3 -> step4 -> step5;
                }
                """
            )

        with data_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    Cloud [shape=box, style=filled, color=lightblue];
                    Edge [shape=box, style=filled, color=lightgrey];
                    Things [shape=box, style=filled, color=lightyellow];

                    Cloud -> Edge [label="Bulk data / models"];
                    Edge -> Things [label="Filtered data / commands"];
                    Things -> Edge [label="Raw telemetry"];
                    Edge -> Cloud [label="Aggregated metrics"];
                }
                """
            )

        with control_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    CloudCtrl [label="Cloud Control", shape=box, style=filled, color=lightblue];
                    EdgeCtrl [label="Edge Orchestrator", shape=box, style=filled, color=lightgrey];
                    ThingsCtrl [label="Device Agents", shape=box, style=filled, color=lightyellow];

                    CloudCtrl -> EdgeCtrl [label="Policies / configs"];
                    EdgeCtrl -> ThingsCtrl [label="Commands / updates"];
                    ThingsCtrl -> EdgeCtrl [label="Status / health"];
                    EdgeCtrl -> CloudCtrl [label="Reports / logs"];
                }
                """
            )

        with interaction_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    Cloud [shape=box, style=filled, color=lightblue];
                    Edge [shape=box, style=filled, color=lightgrey];

                    Cloud -> Edge [label="Tasks, models, policies"];
                    Edge -> Cloud [label="Aggregated results, feedback"];
                }
                """
            )

        with security_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    CloudSec [label="Cloud Security", shape=box, style=filled, color=lightblue];
                    EdgeSec [label="Edge Security", shape=box, style=filled, color=lightgrey];
                    DeviceSec [label="Device Security", shape=box, style=filled, color=lightyellow];

                    CloudSec -> EdgeSec [label="Trust / certs"];
                    EdgeSec -> DeviceSec [label="Auth / encryption"];
                    DeviceSec -> EdgeSec [label="Logs / anomalies"];
                    EdgeSec -> CloudSec [label="Security telemetry"];
                }
                """
            )

    # ----------------- PULL FROM IOT -----------------
    elif sub.startswith("2"):
        st.markdown("### Pull from IoT")
        add_line(
            "1. Almost all kinds of electrical devices will become part of IoT, and they will play the role "
            "of data producers as well as consumers, such as air quality sensors, LED bars, streetlights and "
            "even an Internet-connected microwave oven."
        )
        add_line(
            "2. The number of things at the edge of the network will develop to more than billions in a few years."
        )
        add_line(
            "3. Raw data produced by things will be enormous, making conventional cloud computing not efficient "
            "enough to handle all these data."
        )
        add_line(
            "4. Most of the data produced by IoT will never be transmitted to the cloud, instead it will be "
            "consumed at the edge of the network."
        )
        add_line(
            "5. Most of the end nodes in IoT are energy constrained things, and the wireless communication module "
            "is usually very energy hungry, so offloading some computing tasks to the edge could be more energy efficient."
        )

        concept_tab, flow_tab, data_tab, control_tab, interaction_tab, security_tab = framework_tabs()

        with concept_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    Things [shape=box, style=filled, color=lightyellow, label="IoT Things"];
                    Edge [shape=box, style=filled, color=lightgrey, label="Edge Node / Gateway"];
                    LocalApps [shape=box, style=filled, color=lightgreen, label="Local Apps / Services"];
                    Cloud [shape=box, style=filled, color=lightblue];

                    Things -> Edge [label="Sensor data"];
                    Edge -> LocalApps [label="Insights / control"];
                    Edge -> Cloud [label="Summaries"];
                    Cloud -> Edge [label="Policies / models"];
                }
                """
            )

        with flow_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=TB;
                    step1 [label="1. Things generate raw data", shape=box];
                    step2 [label="2. Edge pulls data from Things", shape=box];
                    step3 [label="3. Edge processes and filters data", shape=box];
                    step4 [label="4. Local apps consume processed data", shape=box];
                    step5 [label="5. Edge sends aggregates to Cloud", shape=box];

                    step1 -> step2 -> step3 -> step4 -> step5;
                }
                """
            )

        with data_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    Things [shape=box, style=filled, color=lightyellow];
                    Edge [shape=box, style=filled, color=lightgrey];
                    Cloud [shape=box, style=filled, color=lightblue];

                    Things -> Edge [label="Continuous sensor streams"];
                    Edge -> Cloud [label="Aggregated / compressed data"];
                    Cloud -> Edge [label="Models / thresholds"];
                }
                """
            )

        with control_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    CloudCtrl [label="Cloud Control", shape=box, style=filled, color=lightblue];
                    EdgeCtrl [label="Edge Controller", shape=box, style=filled, color=lightgrey];
                    ThingsCtrl [label="Device Agents", shape=box, style=filled, color=lightyellow];

                    CloudCtrl -> EdgeCtrl [label="Rules / policies"];
                    EdgeCtrl -> ThingsCtrl [label="Sampling rates / modes"];
                    ThingsCtrl -> EdgeCtrl [label="Status / alarms"];
                    EdgeCtrl -> CloudCtrl [label="Aggregated health / KPIs"];
                }
                """
            )

        with interaction_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    Cloud [shape=box, style=filled, color=lightblue];
                    Edge [shape=box, style=filled, color=lightgrey];

                    Edge -> Cloud [label="Aggregated sensor data"];
                    Cloud -> Edge [label="Updated models / policies"];
                }
                """
            )

        with security_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    CloudSec [label="Cloud Security", shape=box, style=filled, color=lightblue];
                    EdgeSec [label="Edge Security", shape=box, style=filled, color=lightgrey];
                    DeviceSec [label="IoT Device Security", shape=box, style=filled, color=lightyellow];

                    CloudSec -> EdgeSec [label="Policies / certs"];
                    EdgeSec -> DeviceSec [label="Keys / auth"];
                    DeviceSec -> EdgeSec [label="Alerts / anomalies"];
                    EdgeSec -> CloudSec [label="Security posture"];
                }
                """
            )

    # ----------------- CHANGE FROM DATA CONSUMER TO PRODUCER -----------------
    else:
        st.markdown("### Change from Data Consumer to Producer")
        add_line(
            "1. In the cloud computing paradigm, the end devices at the edge usually play as data consumer, "
            "for example, watching a YouTube video on your smart phone."
        )
        add_line(
            "2. However, people are also producing data nowadays from their mobile devices."
        )
        add_line(
            "3. The change from data consumer to data producer/consumer requires more function placement at the edge."
        )
        add_line(
            "4. The image or video clip could be fairly large and it would occupy a lot of bandwidth for uploading. "
            "In this case, the video clip should be demised and adjusted to suitable resolution at the edge before "
            "uploading to cloud. Another example would be wearable health devices."
        )
        add_line(
            "5. Since the physical data collected by the things at the edge of the network is usually private, "
            "processing the data at the edge could protect user privacy better than uploading raw data to cloud."
        )

        concept_tab, flow_tab, data_tab, control_tab, interaction_tab, security_tab = framework_tabs()

        with concept_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    Cloud [shape=box, style=filled, color=lightblue];
                    Device [shape=box, style=filled, color=lightyellow, label="Mobile / Wearable Device"];
                    Edge [shape=box, style=filled, color=lightgrey];

                    Cloud -> Device [label="Content / services"];
                    Device -> Cloud [label="User data"];
                    Device -> Edge [label="Raw sensor / video / health data"];
                    Edge -> Cloud [label="Filtered / anonymized data"];
                    Edge -> Device [label="Real-time insights"];
                }
                """
            )

        with flow_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=TB;
                    step1 [label="1. Device consumes cloud content", shape=box];
                    step2 [label="2. Device starts producing rich data", shape=box];
                    step3 [label="3. Raw data sent to Edge", shape=box];
                    step4 [label="4. Edge processes / anonymizes data", shape=box];
                    step5 [label="5. Edge sends insights to Device and Cloud", shape=box];

                    step1 -> step2 -> step3 -> step4 -> step5;
                }
                """
            )

        with data_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    Device [shape=box, style=filled, color=lightyellow];
                    Edge [shape=box, style=filled, color=lightgrey];
                    Cloud [shape=box, style=filled, color=lightblue];

                    Device -> Edge [label="High-volume sensor / media data"];
                    Edge -> Cloud [label="Summaries / anonymized data"];
                    Cloud -> Edge [label="Models / personalization"];
                    Edge -> Device [label="Real-time feedback"];
                }
                """
            )

        with control_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    CloudCtrl [label="Cloud Personalization Engine", shape=box, style=filled, color=lightblue];
                    EdgeCtrl [label="Edge Privacy / Policy Engine", shape=box, style=filled, color=lightgrey];
                    DeviceCtrl [label="Device App / Agent", shape=box, style=filled, color=lightyellow];

                    CloudCtrl -> EdgeCtrl [label="Global policies"];
                    EdgeCtrl -> DeviceCtrl [label="Local rules / consent"];
                    DeviceCtrl -> EdgeCtrl [label="User preferences"];
                    EdgeCtrl -> CloudCtrl [label="Compliance / audit logs"];
                }
                """
            )

        with interaction_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    Cloud [shape=box, style=filled, color=lightblue];
                    Edge [shape=box, style=filled, color=lightgrey];

                    Edge -> Cloud [label="Anonymized / aggregated user data"];
                    Cloud -> Edge [label="Updated personalization models"];
                }
                """
            )

        with security_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    CloudSec [label="Cloud Privacy / Security", shape=box, style=filled, color=lightblue];
                    EdgeSec [label="Edge Privacy Guard", shape=box, style=filled, color=lightgrey];
                    DeviceSec [label="Device Security / Consent", shape=box, style=filled, color=lightyellow];

                    CloudSec -> EdgeSec [label="Privacy policies"];
                    EdgeSec -> DeviceSec [label="Consent enforcement"];
                    DeviceSec -> EdgeSec [label="User choices"];
                    EdgeSec -> CloudSec [label="Compliance reports"];
                }
                """
            )

# ------------------------------------------------------------------------------------
# USE CASES
# ------------------------------------------------------------------------------------
elif main_category.startswith("2"):
    st.markdown("## Edge-Computing Use Cases")

    sub = st.selectbox(
        "Select Use Case:",
        [
            "1. Cloud Offloading",
            "2. Video Analytics",
            "3. Smart Home",
            "4. Smart City",
            "5. Collaborative Edge",
            "6. Industrial IoT (Expanded)",
        ],
    )

    concept_tab, flow_tab, data_tab, control_tab, interaction_tab, security_tab = framework_tabs()

    # ----------------- CLOUD OFFLOADING -----------------
    if sub.startswith("1"):
        st.markdown("### Use Case 1: Cloud Offloading")
        add_line(
            "1. In the cloud computing paradigm, most of the computations happen in the cloud, which means data "
            "and requests are processed in the centralized cloud, such a computing paradigm may suffer longer "
            "latency which weakens the user experience."
        )
        add_line(
            "2. In edge computing, the edge has certain computation resources, and this provides a chance to offload "
            "part of the workload from cloud."
        )
        add_line(
            "3. In the IoT, the data is produced and consumed at the edge. Thus, in the edge computing paradigm, "
            "not only data but also operations applied on the data should be cached at the edge."
        )
        add_line(
            "4. The data at the edge node should be synchronized with the cloud, however, this can be done in the background."
        )
        add_line(
            "5. Navigation applications can move the navigating or searching services to the edge for a local area, "
            "in which case only a few map blocks are involved."
        )
        add_line(
            "6. Content filtering/aggregating could be done at the edge nodes to reduce the data volume to be transferred."
        )
        add_line(
            "7. Real-time applications such as vision-aid entertainment games, augmented reality, and connected health, "
            "could make fast responses by using edge nodes."
        )
        add_line(
            "8. By leveraging edge computing, the latency and consequently the user experience for time-sensitive "
            "application could be improved significantly."
        )

        with concept_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    User [shape=box, style=filled, color=lightyellow];
                    Edge [shape=box, style=filled, color=lightgrey];
                    Cloud [shape=box, style=filled, color=lightblue];

                    User -> Edge [label="Requests / data"];
                    Edge -> Cloud [label="Offloaded heavy tasks"];
                    Cloud -> Edge [label="Models / updates"];
                    Edge -> User [label="Low-latency responses"];
                }
                """
            )

        with flow_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=TB;
                    step1 [label="1. User sends request", shape=box];
                    step2 [label="2. Edge handles time-sensitive part", shape=box];
                    step3 [label="3. Edge offloads heavy tasks to Cloud", shape=box];
                    step4 [label="4. Cloud processes and returns models", shape=box];
                    step5 [label="5. Edge responds quickly to User", shape=box];

                    step1 -> step2 -> step3 -> step4 -> step5;
                }
                """
            )

        with data_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    User [shape=box, style=filled, color=lightyellow];
                    Edge [shape=box, style=filled, color=lightgrey];
                    Cloud [shape=box, style=filled, color=lightblue];

                    User -> Edge [label="Requests / small data"];
                    Edge -> Cloud [label="Batch / heavy data"];
                    Cloud -> Edge [label="Models / large artifacts"];
                    Edge -> User [label="Responses / results"];
                }
                """
            )

        with control_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    CloudCtrl [label="Cloud Orchestrator", shape=box, style=filled, color=lightblue];
                    EdgeCtrl [label="Edge Scheduler", shape=box, style=filled, color=lightgrey];

                    CloudCtrl -> EdgeCtrl [label="Offload policies"];
                    EdgeCtrl -> CloudCtrl [label="Load / capacity reports"];
                }
                """
            )

        with interaction_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    Cloud [shape=box, style=filled, color=lightblue];
                    Edge [shape=box, style=filled, color=lightgrey];

                    Edge -> Cloud [label="Offloaded workloads"];
                    Cloud -> Edge [label="Processed results / models"];
                }
                """
            )

        with security_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    CloudSec [label="Cloud Security", shape=box, style=filled, color=lightblue];
                    EdgeSec [label="Edge Security", shape=box, style=filled, color=lightgrey];

                    CloudSec -> EdgeSec [label="Secure channels / policies"];
                    EdgeSec -> CloudSec [label="Audit / logs"];
                }
                """
            )

    # ----------------- VIDEO ANALYTICS -----------------
    elif sub.startswith("2"):
        st.markdown("### Use Case 2: Video Analytics")
        add_line(
            "1. The widespread of mobile phones and network cameras make video analytics an emerging technology."
        )
        add_line(
            "2. Cloud computing is no longer suitable for applications that require video analytics due to the long "
            "data transmission latency and privacy concerns."
        )
        add_line(
            "3. The data from the camera will usually not be uploaded to the cloud because of privacy issues or "
            "traffic cost, which makes it extremely difficult to leverage the wide area camera data."
        )
        add_line(
            "4. Even if the data is accessible on the cloud, uploading and searching a huge quantity of data could take a long time."
        )
        add_line(
            "5. Each thing, for example, a smart phone, can perform the request and search its local camera data and only "
            "report the result back to the cloud."
        )
        add_line(
            "6. In this paradigm, it is possible to leverage the data and computing power on every thing and get the result "
            "much faster compared with solitary cloud computing."
        )

        with concept_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    Camera [shape=box, style=filled, color=lightyellow];
                    Edge [shape=box, style=filled, color=lightgrey];
                    LocalAI [shape=box, style=filled, color=lightgreen];
                    Cloud [shape=box, style=filled, color=lightblue];

                    Camera -> Edge [label="Raw video"];
                    Edge -> LocalAI [label="Frames / features"];
                    LocalAI -> Edge [label="Detections / events"];
                    Edge -> Cloud [label="Summaries / alerts"];
                }
                """
            )

        with flow_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=TB;
                    step1 [label="1. Camera captures video", shape=box];
                    step2 [label="2. Edge receives stream", shape=box];
                    step3 [label="3. Edge / Local AI analyze frames", shape=box];
                    step4 [label="4. Edge generates events / alerts", shape=box];
                    step5 [label="5. Edge sends summaries to Cloud", shape=box];

                    step1 -> step2 -> step3 -> step4 -> step5;
                }
                """
            )

        with data_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    Camera [shape=box, style=filled, color=lightyellow];
                    Edge [shape=box, style=filled, color=lightgrey];
                    Cloud [shape=box, style=filled, color=lightblue];

                    Camera -> Edge [label="High-bandwidth video"];
                    Edge -> Cloud [label="Low-bandwidth events / metadata"];
                }
                """
            )

        with control_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    CloudCtrl [label="Cloud Analytics Config", shape=box, style=filled, color=lightblue];
                    EdgeCtrl [label="Edge Analytics Engine", shape=box, style=filled, color=lightgrey];
                    CameraCtrl [label="Camera Settings", shape=box, style=filled, color=lightyellow];

                    CloudCtrl -> EdgeCtrl [label="Models / thresholds"];
                    EdgeCtrl -> CameraCtrl [label="FPS / resolution / zones"];
                    EdgeCtrl -> CloudCtrl [label="Performance / accuracy stats"];
                }
                """
            )

        with interaction_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    Cloud [shape=box, style=filled, color=lightblue];
                    Edge [shape=box, style=filled, color=lightgrey];

                    Edge -> Cloud [label="Alerts / summaries"];
                    Cloud -> Edge [label="Updated models / rules"];
                }
                """
            )

        with security_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    CloudSec [label="Cloud Security", shape=box, style=filled, color=lightblue];
                    EdgeSec [label="Edge Security", shape=box, style=filled, color=lightgrey];
                    CameraSec [label="Camera Security", shape=box, style=filled, color=lightyellow];

                    CloudSec -> EdgeSec [label="Model integrity"];
                    EdgeSec -> CameraSec [label="Secure streaming"];
                    CameraSec -> EdgeSec [label="Tamper alerts"];
                }
                """
            )

    # ----------------- SMART HOME -----------------
    elif sub.startswith("3"):
        st.markdown("### Use Case 3: Smart Home")
        add_line(
            "1. IoT would benefit the home environment a lot. Some products have been developed and are available on the "
            "market such as smart light, smart TV, and robot vacuum."
        )
        add_line(
            "2. Just adding a Wi-Fi module to the current electrical device and connecting it to the cloud is not enough "
            "for a smart home. In a smart home environment, besides the connected device, cheap wireless sensors and "
            "controllers should be deployed to room, pipe, and even floor and wall."
        )
        add_line(
            "3. These things would report an impressive amount of data and for the consideration of data transportation "
            "pressure and privacy protection, this data should be mostly consumed in the home."
        )
        add_line(
            "4. This feature makes the cloud computing paradigm unsuitable for a smart home therefore edge computing is "
            "considered perfect for building a smart home."
        )
        add_line(
            "5. With an edge gateway running a specialized edge operating system (edgeOS) in the home, the things can be "
            "connected and managed easily in the home, the data can be processed locally to release the burdens for "
            "Internet bandwidth, and the service can also be deployed on the edgeOS for better management and delivery."
        )

        with concept_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    Sensors [shape=box, style=filled, color=lightyellow];
                    EdgeGateway [shape=box, style=filled, color=lightgrey];
                    LocalServices [shape=box, style=filled, color=lightgreen];
                    Cloud [shape=box, style=filled, color=lightblue];
                    UserApp [shape=box, style=filled, color=lightyellow];

                    Sensors -> EdgeGateway [label="Telemetry"];
                    EdgeGateway -> LocalServices [label="Rules / automation"];
                    EdgeGateway -> Cloud [label="Aggregated data"];
                    UserApp -> EdgeGateway [label="Control / monitoring"];
                }
                """
            )

        with flow_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=TB;
                    step1 [label="1. Sensors collect home data", shape=box];
                    step2 [label="2. Edge gateway receives data", shape=box];
                    step3 [label="3. Edge applies rules / automation", shape=box];
                    step4 [label="4. User app interacts with Edge", shape=box];
                    step5 [label="5. Edge sends aggregates to Cloud", shape=box];

                    step1 -> step2 -> step3 -> step4 -> step5;
                }
                """
            )

        with data_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    Sensors [shape=box, style=filled, color=lightyellow];
                    EdgeGateway [shape=box, style=filled, color=lightgrey];
                    Cloud [shape=box, style=filled, color=lightblue];

                    Sensors -> EdgeGateway [label="Local telemetry"];
                    EdgeGateway -> Cloud [label="Aggregated / periodic data"];
                    Cloud -> EdgeGateway [label="Global updates / services"];
                }
                """
            )

        with control_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    CloudCtrl [label="Cloud Smart Home Service", shape=box, style=filled, color=lightblue];
                    EdgeCtrl [label="Home Edge Gateway", shape=box, style=filled, color=lightgrey];
                    UserCtrl [label="User App", shape=box, style=filled, color=lightyellow];

                    CloudCtrl -> EdgeCtrl [label="Feature configs / firmware"];
                    UserCtrl -> EdgeCtrl [label="Preferences / scenes"];
                    EdgeCtrl -> CloudCtrl [label="Status / diagnostics"];
                }
                """
            )

        with interaction_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    Cloud [shape=box, style=filled, color=lightblue];
                    Edge [shape=box, style=filled, color=lightgrey];

                    Edge -> Cloud [label="Home metrics / logs"];
                    Cloud -> Edge [label="New capabilities / updates"];
                }
                """
            )

        with security_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    CloudSec [label="Cloud Security", shape=box, style=filled, color=lightblue];
                    EdgeSec [label="Home Gateway Security", shape=box, style=filled, color=lightgrey];
                    DeviceSec [label="Device Security", shape=box, style=filled, color=lightyellow];

                    CloudSec -> EdgeSec [label="Policies / patches"];
                    EdgeSec -> DeviceSec [label="Local auth / encryption"];
                    DeviceSec -> EdgeSec [label="Alerts / logs"];
                }
                """
            )

    # ----------------- SMART CITY -----------------
    elif sub.startswith("4"):
        st.markdown("### Use Case 4: Smart City")
        add_line(
            "1. The edge computing paradigm can be flexibly expanded from a single home to community, or even city scale. "
            "Edge computing claims that computing should happen as close as possible to the data source."
        )
        add_line(
            "2. With this design, a request could be generated from the top of the computing paradigm and be actually "
            "processed at the edge."
        )
        add_line(
            "3. Edge computing could be an ideal platform for smart city considering the following characteristics:"
        )
        add_line(
            "   A. Large-Data-Quantity: A city populated by 1 million people will produce huge data per day, contributed "
            "by public safety, health, utility, and transports. Centralized cloud alone is unrealistic; edge processing "
            "is needed."
        )
        add_line(
            "   B. Low-Latency: For applications that require predictable and low latency such as health emergency or "
            "public safety."
        )
        add_line(
            "   C. Location-Awareness: For geographic-based applications such as transportation and utility management, "
            "edge computing exceeds cloud computing due to location awareness."
        )

        with concept_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    CitySensors [shape=box, style=filled, color=lightyellow];
                    DistrictEdge [shape=box, style=filled, color=lightgrey];
                    CityEdge [shape=box, style=filled, color=lightgrey];
                    Cloud [shape=box, style=filled, color=lightblue];
                    OpsCenter [shape=box, style=filled, color=lightgreen, label="City Ops Center"];

                    CitySensors -> DistrictEdge;
                    DistrictEdge -> CityEdge;
                    CityEdge -> Cloud;
                    Cloud -> OpsCenter;
                }
                """
            )

        with flow_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=TB;
                    step1 [label="1. City sensors collect data", shape=box];
                    step2 [label="2. District edge nodes process locally", shape=box];
                    step3 [label="3. City edge aggregates and optimizes", shape=box];
                    step4 [label="4. Cloud stores and analyzes long-term", shape=box];
                    step5 [label="5. Ops center uses insights for decisions", shape=box];

                    step1 -> step2 -> step3 -> step4 -> step5;
                }
                """
            )

        with data_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    CitySensors [shape=box, style=filled, color=lightyellow];
                    DistrictEdge [shape=box, style=filled, color=lightgrey];
                    CityEdge [shape=box, style=filled, color=lightgrey];
                    Cloud [shape=box, style=filled, color=lightblue];

                    CitySensors -> DistrictEdge [label="Local sensor data"];
                    DistrictEdge -> CityEdge [label="Aggregated regional data"];
                    CityEdge -> Cloud [label="City-wide metrics"];
                }
                """
            )

        with control_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    CloudCtrl [label="National / Central Control", shape=box, style=filled, color=lightblue];
                    CityCtrl [label="City Ops Center", shape=box, style=filled, color=lightgreen];
                    EdgeCtrl [label="District Edge Controllers", shape=box, style=filled, color=lightgrey];

                    CloudCtrl -> CityCtrl [label="Policies / regulations"];
                    CityCtrl -> EdgeCtrl [label="Operational rules"];
                    EdgeCtrl -> CityCtrl [label="Status / incidents"];
                }
                """
            )

        with interaction_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    Cloud [shape=box, style=filled, color=lightblue];
                    CityEdge [shape=box, style=filled, color=lightgrey];

                    CityEdge -> Cloud [label="City metrics / KPIs"];
                    Cloud -> CityEdge [label="Benchmarking / optimization models"];
                }
                """
            )

        with security_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    CloudSec [label="Central Security", shape=box, style=filled, color=lightblue];
                    CitySec [label="City Security Ops", shape=box, style=filled, color=lightgreen];
                    EdgeSec [label="District Edge Security", shape=box, style=filled, color=lightgrey];

                    CloudSec -> CitySec [label="Policies / threat intel"];
                    CitySec -> EdgeSec [label="Local enforcement"];
                    EdgeSec -> CitySec [label="Incidents / alerts"];
                }
                """
            )

    # ----------------- COLLABORATIVE EDGE -----------------
    elif sub.startswith("5"):
        st.markdown("### Use Case 5: Collaborative Edge")
        add_line(
            "Collaborative edge refers to multiple edge nodes working together to share load, data, and intelligence "
            "across regions or domains."
        )
        add_line(
            "It enables resilience, better resource utilization, and cross-domain analytics without centralizing all data."
        )

        with concept_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    Edge1 [shape=box, style=filled, color=lightgrey];
                    Edge2 [shape=box, style=filled, color=lightgrey];
                    Edge3 [shape=box, style=filled, color=lightgrey];
                    Cloud [shape=box, style=filled, color=lightblue];

                    Edge1 -> Edge2 [label="Data / tasks"];
                    Edge2 -> Edge3 [label="Models / insights"];
                    Edge3 -> Cloud [label="Aggregated results"];
                    Cloud -> Edge1 [label="Global policies"];
                }
                """
            )

        with flow_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=TB;
                    step1 [label="1. Edge nodes receive local workloads", shape=box];
                    step2 [label="2. Edges share tasks / data among peers", shape=box];
                    step3 [label="3. Collaborative processing across edges", shape=box];
                    step4 [label="4. Aggregated results sent to Cloud", shape=box];
                    step5 [label="5. Cloud distributes global policies back", shape=box];

                    step1 -> step2 -> step3 -> step4 -> step5;
                }
                """
            )

        with data_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    Edge1 [shape=box, style=filled, color=lightgrey];
                    Edge2 [shape=box, style=filled, color=lightgrey];
                    Edge3 [shape=box, style=filled, color=lightgrey];

                    Edge1 -> Edge2 [label="Shared datasets"];
                    Edge2 -> Edge3 [label="Model parameters"];
                    Edge3 -> Edge1 [label="Aggregated insights"];
                }
                """
            )

        with control_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    CloudCtrl [label="Global Coordinator", shape=box, style=filled, color=lightblue];
                    EdgeCtrl1 [label="Edge Controller 1", shape=box, style=filled, color=lightgrey];
                    EdgeCtrl2 [label="Edge Controller 2", shape=box, style=filled, color=lightgrey];

                    CloudCtrl -> EdgeCtrl1 [label="Policies / roles"];
                    CloudCtrl -> EdgeCtrl2 [label="Policies / roles"];
                    EdgeCtrl1 -> EdgeCtrl2 [label="Coordination / negotiation"];
                }
                """
            )

        with interaction_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    Cloud [shape=box, style=filled, color=lightblue];
                    EdgeCluster [shape=box, style=filled, color=lightgrey, label="Edge Cluster"];

                    EdgeCluster -> Cloud [label="Cluster-wide results"];
                    Cloud -> EdgeCluster [label="Global optimization / policies"];
                }
                """
            )

        with security_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    CloudSec [label="Global Security", shape=box, style=filled, color=lightblue];
                    EdgeSec1 [label="Edge Security 1", shape=box, style=filled, color=lightgrey];
                    EdgeSec2 [label="Edge Security 2", shape=box, style=filled, color=lightgrey];

                    CloudSec -> EdgeSec1 [label="Policies"];
                    CloudSec -> EdgeSec2 [label="Policies"];
                    EdgeSec1 -> EdgeSec2 [label="Trust / federation"];
                }
                """
            )

    # ----------------- INDUSTRIAL IOT -----------------
    else:
        st.markdown("### Use Case 6: Industrial IoT (Expanded)")
        add_line(
            "Industrial IoT (IIoT) uses edge computing to process sensor data from machines, robots, and production lines "
            "in real time."
        )
        add_line(
            "Edge nodes perform anomaly detection, predictive maintenance, and safety monitoring close to the equipment, "
            "reducing latency and bandwidth usage."
        )
        add_line(
            "Aggregated insights and historical data are sent to the cloud for long-term analytics, optimization, and "
            "fleet-wide learning."
        )

        with concept_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    Machines [shape=box, style=filled, color=lightyellow];
                    EdgeNode [shape=box, style=filled, color=lightgrey];
                    PlantControl [shape=box, style=filled, color=lightgreen];
                    Cloud [shape=box, style=filled, color=lightblue];

                    Machines -> EdgeNode [label="Sensor data"];
                    EdgeNode -> PlantControl [label="Alerts / recommendations"];
                    EdgeNode -> Cloud [label="Aggregated metrics"];
                    Cloud -> PlantControl [label="Global optimization / models"];
                }
                """
            )

        with flow_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=TB;
                    step1 [label="1. Machines emit sensor data", shape=box];
                    step2 [label="2. Edge node ingests and analyzes", shape=box];
                    step3 [label="3. Edge triggers local actions / alerts", shape=box];
                    step4 [label="4. Edge sends metrics to Cloud", shape=box];
                    step5 [label="5. Cloud refines models and sends back", shape=box];

                    step1 -> step2 -> step3 -> step4 -> step5;
                }
                """
            )

        with data_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    Machines [shape=box, style=filled, color=lightyellow];
                    EdgeNode [shape=box, style=filled, color=lightgrey];
                    Cloud [shape=box, style=filled, color=lightblue];

                    Machines -> EdgeNode [label="High-frequency sensor data"];
                    EdgeNode -> Cloud [label="Aggregated KPIs / events"];
                    Cloud -> EdgeNode [label="Updated models / thresholds"];
                }
                """
            )

        with control_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    CloudCtrl [label="Fleet Management", shape=box, style=filled, color=lightblue];
                    EdgeCtrl [label="Plant Edge Controller", shape=box, style=filled, color=lightgrey];
                    MachineCtrl [label="Machine PLC / Agent", shape=box, style=filled, color=lightyellow];

                    CloudCtrl -> EdgeCtrl [label="Global policies / schedules"];
                    EdgeCtrl -> MachineCtrl [label="Local control / overrides"];
                    MachineCtrl -> EdgeCtrl [label="Status / alarms"];
                    EdgeCtrl -> CloudCtrl [label="Plant KPIs / incidents"];
                }
                """
            )

        with interaction_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    Cloud [shape=box, style=filled, color=lightblue];
                    Edge [shape=box, style=filled, color=lightgrey];

                    Edge -> Cloud [label="Plant metrics / events"];
                    Cloud -> Edge [label="Optimization strategies / models"];
                }
                """
            )

        with security_tab:
            st.graphviz_chart(
                """
                digraph {
                    rankdir=LR;
                    CloudSec [label="Fleet Security", shape=box, style=filled, color=lightblue];
                    EdgeSec [label="Plant Security", shape=box, style=filled, color=lightgrey];
                    MachineSec [label="Machine Security", shape=box, style=filled, color=lightyellow];

                    CloudSec -> EdgeSec [label="Policies / threat intel"];
                    EdgeSec -> MachineSec [label="Local enforcement"];
                    MachineSec -> EdgeSec [label="Incidents / alerts"];
                }
                """
            )

# ------------------------------------------------------------------------------------
# FRAMEWORK CHALLENGES
# ------------------------------------------------------------------------------------
elif main_category.startswith("3"):
    st.markdown("## Edge-Computing Framework Challenges")

    sub = st.selectbox(
        "Select Challenge Category:",
        [
            "Programmability",
            "Naming",
            "Data Abstraction",
            "Service Management",
            "Privacy & Security",
            "Optimization Metrics",
        ],
    )

    st.markdown(f"### {sub} Challenge")
    add_line(
        "This section captures key challenges in designing and operating an edge-computing framework, "
        "including architectural complexity, interoperability, and operational risk."
    )
    add_line(
        "You can extend this area with more detailed text, diagrams, and metrics specific to your framework."
    )

    concept_tab, flow_tab, data_tab, control_tab, interaction_tab, security_tab = framework_tabs()

    with flow_tab:
        st.graphviz_chart(
            """
            digraph {
                rankdir=TB;
                Requirement -> Design;
                Design -> EdgeNodes;
                EdgeNodes -> Monitoring;
                Monitoring -> Optimization;
            }
            """
        )

    with concept_tab:
        st.graphviz_chart(
            """
            digraph {
                rankdir=LR;
                Requirement [shape=box];
                Design [shape=box];
                EdgeNodes [shape=box];
                Cloud [shape=box];

                Requirement -> Design;
                Design -> EdgeNodes;
                EdgeNodes -> Cloud;
            }
            """
        )

    with data_tab:
        st.graphviz_chart(
            """
            digraph {
                rankdir=LR;
                EdgeNodes [shape=box];
                Cloud [shape=box];

                EdgeNodes -> Cloud [label="Metrics / logs"];
                Cloud -> EdgeNodes [label="Configs / policies"];
            }
            """
        )

    with control_tab:
        st.graphviz_chart(
            """
            digraph {
                rankdir=LR;
                Orchestrator [shape=box];
                EdgeNodes [shape=box];

                Orchestrator -> EdgeNodes [label="Control commands"];
                EdgeNodes -> Orchestrator [label="Status / feedback"];
            }
            """
        )

    with interaction_tab:
        st.graphviz_chart(
            """
            digraph {
                rankdir=LR;
                Cloud [shape=box];
                Edge [shape=box];

                Cloud -> Edge [label="Policies / updates"];
                Edge -> Cloud [label="Telemetry / KPIs"];
            }
            """
        )

    with security_tab:
        st.graphviz_chart(
            """
            digraph {
                rankdir=LR;
                SecPolicy [shape=box, label="Security Policy"];
                EdgeSec [shape=box, label="Edge Security"];
                CloudSec [shape=box, label="Cloud Security"];

                SecPolicy -> EdgeSec;
                SecPolicy -> CloudSec;
                EdgeSec -> CloudSec [label="Incidents / alerts"];
            }
            """
        )

# ------------------------------------------------------------------------------------
# TAXONOMY MATRIX
# ------------------------------------------------------------------------------------
else:
    st.markdown("## Taxonomy Matrix – Use Case Comparison")

    data = {
        "Use Case": [
            "Cloud Offloading",
            "Video Analytics",
            "Smart Home",
            "Smart City",
            "Collaborative Edge",
            "Industrial IoT",
        ],
        "Latency Sensitivity": [
            "High",
            "High",
            "Medium",
            "High",
            "Medium",
            "High",
        ],
        "Privacy Sensitivity": [
            "Medium",
            "High",
            "High",
            "High",
            "Medium",
            "High",
        ],
        "Bandwidth Pressure": [
            "High",
            "High",
            "Medium",
            "High",
            "Medium",
            "High",
        ],
        "Edge Compute Intensity": [
            "Medium",
            "High",
            "Medium",
            "High",
            "High",
            "High",
        ],
        "Cloud Dependence": [
            "High",
            "Medium",
            "Medium",
            "High",
            "Medium",
            "High",
        ],
    }

    df = pd.DataFrame(data)
    st.dataframe(df, use_container_width=True)
    current_text_lines.append("Taxonomy matrix comparing use cases by latency, privacy, bandwidth, edge intensity, and cloud dependence.")

# ------------------------------------------------------------------------------------
# EXPORT CURRENT SECTION
# ------------------------------------------------------------------------------------
st.markdown("---")
st.markdown("### Export Current View")

export_col1, export_col2, export_col3 = st.columns(3)

export_text = "\n".join(current_text_lines) if current_text_lines else "No content selected."

with export_col3:
    json_bytes = json.dumps({"category": main_category, "content": current_text_lines}, indent=2).encode("utf-8")
    st.download_button(
        label="Download JSON",
        data=json_bytes,
        file_name="edge_framework_export.json",
        mime="application/json",
    )

with export_col2:
    doc_bytes = export_text.encode("utf-8")
    st.download_button(
        label="Download Word (.doc)",
        data=doc_bytes,
        file_name="edge_framework_export.doc",
        mime="application/msword",
    )

with export_col1:
    pdf_buffer = BytesIO()
    pdf_buffer.write(export_text.encode("utf-8"))
    pdf_buffer.seek(0)
    st.download_button(
        label="Download PDF (text-based)",
        data=pdf_buffer,
        file_name="edge_framework_export.pdf",
        mime="application/pdf",
    )
