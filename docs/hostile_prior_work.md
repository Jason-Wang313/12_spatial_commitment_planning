# Hostile Prior Work Set

This is the 100-paper set most likely to attack novelty. Each entry records the requested extraction fields. The extraction is grounded in title, venue metadata, concepts, and available abstracts in the matrix, not a claim of exhaustive full-text reading.

## 1. Dexterous robotic motion planning using intelligent algorithms
- Year/venue: 2015 / Dialnet (Universidad de la Rioja)
- Problem claimed: The fundamental purpose of robots is to help humans in a variety of difficult tasks, enabling people to increase their capabilities of strength, energy, speed, memory, and to operate in hazardous environments and many other applications.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2533730717

## 2. Constraint Graphs: Unifying task and motion planning for Navigation and Manipulation Among Movable Obstacles
- Year/venue: 2016 / HAL (Le Centre pour la Communication Scientifique Directe)
- Problem claimed: We consider a class of advanced motion planning problems including object manipulation, navigation among movable obtacles and legged locomotion.
- Actual mechanism introduced: integrated symbolic-geometric task/motion planning
- Hidden assumptions: symbolic predicates remain valid across geometric execution; geometric feasibility can be recovered by more samples; objects can be moved without creating unrecoverable access losses; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: integrating symbolic goals with geometric feasibility; planning around object-induced access constraints; motion-space search and narrow-passage exploration
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode; separate rearrangement ordering from reachability loss certificates; lift geometric dead-end cuts into symbolic preconditions without hand-authoring them
- URL: https://openalex.org/W2471394985

## 3. ManipulaTHOR: A Framework for Visual Object Manipulation
- Year/venue: 2021 / 
- Problem claimed: The domain of Embodied AI has recently witnessed substantial progress, particularly in navigating agents within their environments.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W3153322041

## 4. Linear manipulator: Motion control of an n-link robotic arm mounted on a mobile slider
- Year/venue: 2023 / Heliyon
- Problem claimed: Linear manipulators are versatile linear robotics systems that can be reprogrammed to accommodate product changes quickly and are flexible to meet unique requirements.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4315474353

## 5. Versatile multicontact planning and control for legged loco-manipulation
- Year/venue: 2023 / Science Robotics
- Problem claimed: Loco-manipulation planning skills are pivotal for expanding the utility of robots in everyday environments.
- Actual mechanism introduced: integrated symbolic-geometric task/motion planning
- Hidden assumptions: symbolic predicates remain valid across geometric execution; geometric feasibility can be recovered by more samples; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: integrating symbolic goals with geometric feasibility; motion-space search and narrow-passage exploration
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode; lift geometric dead-end cuts into symbolic preconditions without hand-authoring them
- URL: https://openalex.org/W4385858056

## 6. Homotopic Path Set Planning for Robot Manipulation and Navigation
- Year/venue: 2024 / 
- Problem claimed: This paper addresses path set planning that yields important applications in robot manipulation and navigation such as path generation for deformable object keypoints and swarms.A path set refers to the collection of finite agent paths to represent the overall spatial path of a group of keypoints or a swarm, whose collective properties meet spatial and topological constraints.As opposed to planning a single path, sim
- Actual mechanism introduced: sampling-based motion-space exploration
- Hidden assumptions: geometric feasibility can be recovered by more samples; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: motion-space search and narrow-passage exploration
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4402354123

## 7. Stability Analysis and Navigational Techniques of Wheeled Mobile Robot: A Review
- Year/venue: 2023 / Processes
- Problem claimed: Wheeled mobile robots (WMRs) have been a focus of research for several decades, particularly concerning navigation strategies in static and dynamic environments.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4389049365

## 8. M<sup>2</sup> Diffuser: Diffusion-based Trajectory Optimization for Mobile Manipulation in 3D Scenes
- Year/venue: 2025 / IEEE Transactions on Pattern Analysis and Machine Intelligence
- Problem claimed: Recent advances in diffusion models have opened new avenues for research into embodied AI agents and robotics.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4408727266

## 9. An Immunological Approach to Mobile Robot Navigation
- Year/venue: 2008 / InTech eBooks
- Problem claimed: Autonomous mobile robots have a wide range of applications in industries, hospitals, offices, and even the military, due to their superior mobility.
- Actual mechanism introduced: belief-state or uncertainty-aware planning
- Hidden assumptions: uncertainty is the main hidden variable; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: uncertainty-aware variants of planning
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W1597093691

## 10. A review on indoor human aware autonomous mobile robot navigation through a dynamic environment survey of different path planning algorithm and methods
- Year/venue: 2015 / 
- Problem claimed: Practical realistic environment for path and continuous motion planning problems normally consist of numerous working areas such as in indoor application consist of number of bedrooms, hallways, multiple doorways with many static and dynamic obstacle in between.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W1499825025

## 11. Development of a Multifunctional Mobile Manipulation Robot Based on Hierarchical Motion Planning Strategy and Hybrid Grasping
- Year/venue: 2025 / Robotics
- Problem claimed: A mobile manipulation robot combines the navigation capability of unmanned ground vehicles and manipulation advantage of robotic arms.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4413068219

## 12. Motion planning with temporal-logic specifications: Progress and challenges
- Year/venue: 2015 / AI Communications
- Problem claimed: Integrating task and motion planning is becoming increasingly important due to the recognition that a growing number of robotics applications in navigation, search-and-rescue missions, manipulation, and medicine involve reasoning with both discrete abstractions and continuous motions.
- Actual mechanism introduced: integrated symbolic-geometric task/motion planning
- Hidden assumptions: symbolic predicates remain valid across geometric execution; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: integrating symbolic goals with geometric feasibility
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode; lift geometric dead-end cuts into symbolic preconditions without hand-authoring them
- URL: https://openalex.org/W2144588269

## 13. A Survey of Robotic Harvesting Systems and Enabling Technologies
- Year/venue: 2023 / Journal of Intelligent & Robotic Systems
- Problem claimed: This paper presents a comprehensive review of ground agricultural robotic systems and applications with special focus on harvesting that span research and commercial products and results, as well as their enabling technologies.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4318224841

## 14. Fast, Anytime Motion Planning for Prehensile Manipulation in Clutter
- Year/venue: 2018 / 
- Problem claimed: Many methods have been developed for planning the motion of robotic arms for picking and placing, ranging from local optimization to global search techniques, which are effective for sparsely placed objects.
- Actual mechanism introduced: sampling-based motion-space exploration
- Hidden assumptions: geometric feasibility can be recovered by more samples; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: motion-space search and narrow-passage exploration
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2808763600

## 15. Visibility-Aware Navigation Among Movable Obstacles
- Year/venue: 2023 / 
- Problem claimed: In this paper, we examine the problem of visibility-aware robot navigation among movable obstacles (VANAMO).
- Actual mechanism introduced: search over obstacle rearrangements and navigation constraints
- Hidden assumptions: objects can be moved without creating unrecoverable access losses; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: planning around object-induced access constraints
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4383172014

## 16. Perceptive Locomotion for Legged Robots in Rough Terrain
- Year/venue: 2018 / Repository for Publications and Research Data (ETH Zurich)
- Problem claimed: Robotic technologies will continue to enter new applications in addition to automated manufacturing and logistics.
- Actual mechanism introduced: contact/action model for manipulation under geometric constraints
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2888398732

## 17. Go Fetch: Mobile Manipulation in Unstructured Environments
- Year/venue: 2020 / arXiv (Cornell University)
- Problem claimed: With humankind facing new and increasingly large-scale challenges in the medical and domestic spheres, automation of the service sector carries a tremendous potential for improved efficiency, quality, and safety of operations.
- Actual mechanism introduced: planning representation or algorithm for robot action selection
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W3014311254

## 18. Large language models for chemistry robotics
- Year/venue: 2023 / Autonomous Robots
- Problem claimed: Abstract This paper proposes an approach to automate chemistry experiments using robots by translating natural language instructions into robot-executable plans, using large language models together with task and motion planning.
- Actual mechanism introduced: symbolic search with sampled geometric streams
- Hidden assumptions: symbolic predicates remain valid across geometric execution; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: integrating symbolic goals with geometric feasibility
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode; lift geometric dead-end cuts into symbolic preconditions without hand-authoring them
- URL: https://openalex.org/W4387937021

## 19. A Software Architecture for Service Robots Manipulating Objects in Human Environments
- Year/venue: 2020 / IEEE Access
- Problem claimed: This paper presents a software architecture for robots providing manipulation services autonomously in human environments.
- Actual mechanism introduced: integrated symbolic-geometric task/motion planning
- Hidden assumptions: symbolic predicates remain valid across geometric execution; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: integrating symbolic goals with geometric feasibility
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode; lift geometric dead-end cuts into symbolic preconditions without hand-authoring them
- URL: https://openalex.org/W3035991693

## 20. Mobile Robotic Manipulation for Search-and-Fetch Tasks by Integrating Human-Robot Interaction
- Year/venue: 2025 / 
- Problem claimed: The increasing labor shortages in commercial and industrial sectors have driven the development of mobile manipulation robots, which combine the mobility of mobile bases with the dexterity of robotic arms to automate complex tasks.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4413442913

## 21. 3P-LLM: Probabilistic Path Planning using Large Language Model for Autonomous Robot Navigation
- Year/venue: 2024 / arXiv (Cornell University)
- Problem claimed: Much worldly semantic knowledge can be encoded in large language models (LLMs).
- Actual mechanism introduced: sampling-based motion-space exploration
- Hidden assumptions: geometric feasibility can be recovered by more samples; space remains navigable after local motion choices; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: motion-space search and narrow-passage exploration
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4393300626

## 22. Towards Shared Autonomy Applications using Whole-body Control Formulations of Locomanipulation
- Year/venue: 2019 / 
- Problem claimed: While widely studied in robotics for decades, mobile manipulation has recently seen a surge in interest for industrial applications due to increasing demands on flexibility and agility alongside productivity, particularly in small and medium enterprises.
- Actual mechanism introduced: planning representation or algorithm for robot action selection
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2974145894

## 23. Autonomous live working robot navigation with real‐time detection and motion planning system on distribution line
- Year/venue: 2022 / High Voltage
- Problem claimed: Abstract In this study, an autonomous robot navigation system is designed for live working on distribution line.
- Actual mechanism introduced: sampling-based motion-space exploration
- Hidden assumptions: geometric feasibility can be recovered by more samples; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: motion-space search and narrow-passage exploration
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4283032729

## 24. Autonomous agents for real-time animation
- Year/venue: 1999 / 
- Problem claimed: Advances in computing hardware, software, and network technology have enabled a new class of interactive applications involving 3D animated characters to become increasingly feasible.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W20717186

## 25. Learning compositional models of robot skills for task and motion planning
- Year/venue: 2021 / The International Journal of Robotics Research
- Problem claimed: The objective of this work is to augment the basic abilities of a robot by learning to use sensorimotor primitives to solve complex long-horizon manipulation problems.
- Actual mechanism introduced: integrated symbolic-geometric task/motion planning
- Hidden assumptions: symbolic predicates remain valid across geometric execution; geometric feasibility can be recovered by more samples; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: integrating symbolic goals with geometric feasibility; motion-space search and narrow-passage exploration
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode; lift geometric dead-end cuts into symbolic preconditions without hand-authoring them
- URL: https://openalex.org/W3150384095

## 26. Rigid body dynamics simulation for robot motion planning
- Year/venue: 2006 / Infoscience (Ecole Polytechnique Fédérale de Lausanne)
- Problem claimed: The development of robot motion planning algorithms is inherently a challenging task.
- Actual mechanism introduced: sampling-based motion-space exploration
- Hidden assumptions: geometric feasibility can be recovered by more samples; uncertainty is the main hidden variable; space remains navigable after local motion choices; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: motion-space search and narrow-passage exploration; uncertainty-aware variants of planning
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W1590992579

## 27. Robotic Swarm Motion Planning for Load Carrying and Manipulating
- Year/venue: 2020 / IEEE Access
- Problem claimed: Certain species of ants can carry out tasks in dense work spaces while maintaining their ability to accurately manipulate heavy loads, and these advantages are of interest to the robotics community.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W3012171967

## 28. Path Smoothing Techniques in Robot Navigation: State-of-the-Art, Current and Future Challenges
- Year/venue: 2018 / Sensors
- Problem claimed: Robot navigation is an indispensable component of any mobile service robot.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2890807499

## 29. Visually Grounded Task and Motion Planning for Mobile Manipulation
- Year/venue: 2022 / 2022 International Conference on Robotics and Automation (ICRA)
- Problem claimed: Task and motion planning (TAMP) algorithms aim to help robots achieve task-level goals, while maintaining motion-level feasibility.
- Actual mechanism introduced: integrated symbolic-geometric task/motion planning
- Hidden assumptions: symbolic predicates remain valid across geometric execution; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: integrating symbolic goals with geometric feasibility
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode; lift geometric dead-end cuts into symbolic preconditions without hand-authoring them
- URL: https://openalex.org/W4226459265

## 30. Skill Transformer: A Monolithic Policy for Mobile Manipulation
- Year/venue: 2023 / 
- Problem claimed: We present Skill Transformer, an approach for solving long-horizon robotic tasks by combining conditional sequence modeling and skill modularity.
- Actual mechanism introduced: object arrangement ordering and manipulation feasibility search
- Hidden assumptions: objects can be moved without creating unrecoverable access losses; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: planning around object-induced access constraints
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode; separate rearrangement ordering from reachability loss certificates
- URL: https://openalex.org/W4390872260

## 31. Agricultural Harvesting Robot Concept Design and System Components: A Review
- Year/venue: 2023 / AgriEngineering
- Problem claimed: Developing different robotic platforms for farm operations is vital to addressing the increasing world population.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4367181416

## 32. Mobile robotics and 3D printing: addressing challenges in path planning and scalability
- Year/venue: 2024 / Virtual and Physical Prototyping
- Problem claimed: Mobile Additive Manufacturing (MAM) systems are transforming large-scale fabrication across various industries, particularly in building and construction.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4404982834

## 33. Toward fieldable human-scale mobile manipulation using RoMan
- Year/venue: 2020 / 
- Problem claimed: Robots are ideal surrogates for performing tasks that are dull, dirty, and dangerous.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W3018239302

## 34. A Motion-Planning System for a Domestic Service Robot
- Year/venue: 2018 / SPIIRAS Proceedings
- Problem claimed: Service robots are intended to help humans in non-industrial environments such as houses or offices.
- Actual mechanism introduced: planning representation or algorithm for robot action selection
- Hidden assumptions: symbolic predicates remain valid across geometric execution; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2895136648

## 35. Motion Planning for a Humanoid Mobile Manipulator System
- Year/venue: 2019 / International Journal of Humanoid Robotics
- Problem claimed: A high redundant non-holonomic humanoid mobile dual-arm manipulator system (MDAMS) is presented in this paper, where the motion planning to realize “human-like” autonomous navigation and manipulation tasks is studied.
- Actual mechanism introduced: sampling-based motion-space exploration
- Hidden assumptions: geometric feasibility can be recovered by more samples; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: motion-space search and narrow-passage exploration
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2808784381

## 36. A Comprehensive Review of Coverage Path Planning in Robotics Using Classical and Heuristic Algorithms
- Year/venue: 2021 / IEEE Access
- Problem claimed: The small battery capacities of the mobile robot and the un-optimized planning efficiency of the industrial robot bottlenecked the time efficiency and productivity rate of coverage tasks in terms of speed and accuracy, putting a great constraint on the usability of the robot applications in various planning strategies in specific environmental conditions.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: local action feasibility is sufficient for long-horizon planning; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W3197167612

## 37. System integration: Application towards autonomous navigation in cluttered environments
- Year/venue: 2016 / 
- Problem claimed: This paper presents the hardware-software system integration of an intelligent mobile robot for efficient navigation tasks in cluttered indoor environments.
- Actual mechanism introduced: planning representation or algorithm for robot action selection
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2586187740

## 38. Combined Task and Motion Planning for Mobile Manipulation
- Year/venue: 2010 / Proceedings of the International Conference on Automated Planning and Scheduling
- Problem claimed: We present a hierarchical planning system and its application to robotic manipulation.
- Actual mechanism introduced: integrated symbolic-geometric task/motion planning
- Hidden assumptions: symbolic predicates remain valid across geometric execution; uncertainty is the main hidden variable; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: integrating symbolic goals with geometric feasibility; uncertainty-aware variants of planning
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode; lift geometric dead-end cuts into symbolic preconditions without hand-authoring them
- URL: https://openalex.org/W2143936212

## 39. Sampling-Based Robot Motion Planning: A Review
- Year/venue: 2014 / IEEE Access
- Problem claimed: Motion planning is a fundamental research area in robotics.
- Actual mechanism introduced: sampling-based motion-space exploration
- Hidden assumptions: geometric feasibility can be recovered by more samples; uncertainty is the main hidden variable; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: motion-space search and narrow-passage exploration; uncertainty-aware variants of planning
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2055201760

## 40. RMP<i>flow</i>: A Geometric Framework for Generation of Multitask Motion Policies
- Year/venue: 2021 / IEEE Transactions on Automation Science and Engineering
- Problem claimed: Generating robot motion for multiple tasks in dynamic environments is challenging, requiring an algorithm to respond reactively while accounting for complex nonlinear relationships between tasks.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W3140178043

## 41. A Motion Planning Algorithm for Redundant Manipulators Using Rapidly Exploring Randomized Trees and Artificial Potential Fields
- Year/venue: 2021 / IEEE Access
- Problem claimed: This paper presents a novel motion planner for redundant robotic manipulators by utilizing rapidly exploring randomized trees and artificial potential fields.
- Actual mechanism introduced: planning representation or algorithm for robot action selection
- Hidden assumptions: space remains navigable after local motion choices; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W3127875737

## 42. Autonomous Mobile Robots.
- Year/venue: 1986 / Defense Technical Information Center (DTIC)
- Problem claimed: Since 1981 the Mobile Robot laboratory of the Robotics Institute of Carnegie-mellon University has conducted basic research in areas crucial for autonomous robots.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W71395793

## 43. Locally active globally stable dynamical systems: Theory, learning, and experiments
- Year/venue: 2022 / The International Journal of Robotics Research
- Problem claimed: State-dependent dynamical systems (DSs) offer adaptivity, reactivity, and robustness to perturbations in motion planning and physical human–robot interaction tasks.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4210585857

## 44. Anytime motion planning for prehensile manipulation in dense clutter
- Year/venue: 2019 / Advanced Robotics
- Problem claimed: Many methods have been developed for planning the motion of robotic arms for picking and placing, ranging from local optimization to global search techniques, which are effective for sparsely placed objects.
- Actual mechanism introduced: sampling-based motion-space exploration
- Hidden assumptions: geometric feasibility can be recovered by more samples; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: motion-space search and narrow-passage exploration
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2984677241

## 45. Gross motion planning—a survey
- Year/venue: 1992 / ACM Computing Surveys
- Problem claimed: Motion planning is one of the most important areas of robotics research.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: local action feasibility is sufficient for long-horizon planning; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2051626883

## 46. ReLMoGen: Integrating Motion Generation in Reinforcement Learning for Mobile Manipulation
- Year/venue: 2021 / 
- Problem claimed: Many Reinforcement Learning (RL) approaches use joint control signals (positions, velocities, torques) as action space for continuous control tasks.
- Actual mechanism introduced: sampling-based motion-space exploration
- Hidden assumptions: geometric feasibility can be recovered by more samples; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: motion-space search and narrow-passage exploration
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W3206530605

## 47. A Human Aware Mobile Robot Motion Planner
- Year/venue: 2007 / IEEE Transactions on Robotics
- Problem claimed: Robot navigation in the presence of humans raises new issues for motion planning and control when the humans must be taken explicitly into account.
- Actual mechanism introduced: planning representation or algorithm for robot action selection
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2046213647

## 48. Stable Autonomous Robotic Wheelchair Navigation in the Environment With Slope Way
- Year/venue: 2020 / IEEE Transactions on Vehicular Technology
- Problem claimed: In this article, we present a path planning approach that is capable of generating a feasible trajectory for stable robotic wheelchair navigation in the environment with slope way.
- Actual mechanism introduced: sampling-based motion-space exploration
- Hidden assumptions: geometric feasibility can be recovered by more samples; space remains navigable after local motion choices; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: motion-space search and narrow-passage exploration
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W3042565332

## 49. A Robot-Assisted Large-Scale Inspection of Wind Turbine Blades in Manufacturing Using an Autonomous Mobile Manipulator
- Year/venue: 2021 / Applied Sciences
- Problem claimed: Wind energy represents the dominant share of renewable energies.
- Actual mechanism introduced: planning representation or algorithm for robot action selection
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W3207632241

## 50. Environment manipulation planner for humanoid robots using task graph that generates action sequence
- Year/venue: 2005 / 
- Problem claimed: In this paper, we describe a planner for a humanoid robot that is capable of finding a path in an environment with movable objects, whereas previous motion planner only deals with an environment with fixed objects.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2139039898

## 51. A review on path planning ai techniques for mobile robots
- Year/venue: 2023 / Robotic Systems and Applications
- Problem claimed: An Industrial Robot is used in industries for transporting, assembly, manufacturing and many more applications.
- Actual mechanism introduced: learned policy/model used inside planning
- Hidden assumptions: space remains navigable after local motion choices; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4381951482

## 52. Mobile manipulation through an assistive home robot
- Year/venue: 2012 / 
- Problem claimed: We present a mobile manipulation platform operated by a motor-impaired person using input from a head-tracker, single-button mouse.
- Actual mechanism introduced: planning representation or algorithm for robot action selection
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W1964695965

## 53. Multi-robot geometric task-and-motion planning for collaborative manipulation tasks
- Year/venue: 2023 / Autonomous Robots
- Problem claimed: Abstract We address multi-robot geometric task-and-motion planning (MR-GTAMP) problems in synchronous , monotone setups.
- Actual mechanism introduced: integrated symbolic-geometric task/motion planning
- Hidden assumptions: manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: integrating symbolic goals with geometric feasibility
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4388020377

## 54. Continuous methods for motion planning
- Year/venue: 1996 / Scholarly Commons (University of Pennsylvania)
- Problem claimed: Motion planning for a robotic system addresses the problem of finding trajectory and actuator forces that are consistent with a given set of constraints and perform a desired task.
- Actual mechanism introduced: planning representation or algorithm for robot action selection
- Hidden assumptions: manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W1522365498

## 55. ReLMoGen: Leveraging Motion Generation in Reinforcement Learning for Mobile Manipulation
- Year/venue: 2020 / arXiv (Cornell University)
- Problem claimed: Many Reinforcement Learning (RL) approaches use joint control signals (positions, velocities, torques) as action space for continuous control tasks.
- Actual mechanism introduced: sampling-based motion-space exploration
- Hidden assumptions: geometric feasibility can be recovered by more samples; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: motion-space search and narrow-passage exploration
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W3069663381

## 56. Technical Overview of Team DRC‐Hubo@UNLV's Approach to the 2015 DARPA Robotics Challenge Finals
- Year/venue: 2017 / Journal of Field Robotics
- Problem claimed: This paper presents a technical overview of Team DRC‐Hubo@UNLV's approach to the 2015 DARPA Robotics Challenge Finals (DRC‐Finals).
- Actual mechanism introduced: planning representation or algorithm for robot action selection
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2591313121

## 57. Real-time path planning for a robot arm in changing environments
- Year/venue: 2010 / 
- Problem claimed: We present a practical strategy for real-time path planning for articulated robot arms in changing environments by integrating PRM for Changing Environments with 3D sensor data.
- Actual mechanism introduced: planning representation or algorithm for robot action selection
- Hidden assumptions: manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2022115960

## 58. Hypergraph-Based Multi-robot Task and Motion Planning
- Year/venue: 2023 / IEEE Transactions on Robotics
- Problem claimed: In this article, we present a multi-robot task and motion planning method that, when applied to the rearrangement of objects by manipulators, results in solution times up to three orders of magnitude faster than the existing methods and successfully plans for problems with up to 20 objects, more than three times as many objects as comparable methods.
- Actual mechanism introduced: integrated symbolic-geometric task/motion planning
- Hidden assumptions: symbolic predicates remain valid across geometric execution; objects can be moved without creating unrecoverable access losses; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: integrating symbolic goals with geometric feasibility; planning around object-induced access constraints
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode; separate rearrangement ordering from reachability loss certificates; lift geometric dead-end cuts into symbolic preconditions without hand-authoring them
- URL: https://openalex.org/W4386131956

## 59. Inspection and maintenance of industrial infrastructure with autonomous underwater robots
- Year/venue: 2023 / Frontiers in Robotics and AI
- Problem claimed: Underwater infrastructure, such as pipelines, requires regular inspection and maintenance including cleaning, welding of defects and valve-turning or hot-stabbing.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4386169345

## 60. A Robotic Grinding Motion Planning Methodology for a Novel Automatic Seam Bead Grinding Robot Manipulator
- Year/venue: 2020 / IEEE Access
- Problem claimed: Industrial robotics is a continuously developing area of in-depth robotics research, as industrial robots have demonstrated to possess advantages in the robotic automation solutions in the industrial automation applications.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W3016704962

## 61. Motion planning with dynamics awareness for long reach manipulation in aerial robotic systems with two arms
- Year/venue: 2018 / International Journal of Advanced Robotic Systems
- Problem claimed: Human activities in maintenance of industrial plants pose elevated risks as well as significant costs due to the required shutdowns of the facility.
- Actual mechanism introduced: planning representation or algorithm for robot action selection
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2799325041

## 62. Robotic disassembly for end-of-life products focusing on task and motion planning: A comprehensive survey
- Year/venue: 2024 / Journal of Manufacturing Systems
- Problem claimed: The rise of mass production and the resulting accumulation of end-of-life (EoL) products present a growing challenge in waste management and highlight the need for efficient resource recovery.
- Actual mechanism introduced: integrated symbolic-geometric task/motion planning
- Hidden assumptions: symbolic predicates remain valid across geometric execution; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: integrating symbolic goals with geometric feasibility
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode; lift geometric dead-end cuts into symbolic preconditions without hand-authoring them
- URL: https://openalex.org/W4403526028

## 63. 3D Laser Scanner for Underwater Manipulation
- Year/venue: 2018 / Sensors
- Problem claimed: Nowadays, research in autonomous underwater manipulation has demonstrated simple applications like picking an object from the sea floor, turning a valve or plugging and unplugging a connector.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2796340014

## 64. Occupancy-elevation grid: an alternative approach for robotic mapping and navigation
- Year/venue: 2015 / Robotica
- Problem claimed: SUMMARY This paper proposes an alternative environment mapping method for accurate robotic navigation based on 3D information.
- Actual mechanism introduced: planning representation or algorithm for robot action selection
- Hidden assumptions: space remains navigable after local motion choices; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2111161219

## 65. SMT-based synthesis of integrated task and motion plans from plan outlines
- Year/venue: 2014 / 
- Problem claimed: We present a new approach to integrated task and motion planning (ITMP) for robots performing mobile manipulation.
- Actual mechanism introduced: integrated symbolic-geometric task/motion planning
- Hidden assumptions: symbolic predicates remain valid across geometric execution; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: integrating symbolic goals with geometric feasibility
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode; lift geometric dead-end cuts into symbolic preconditions without hand-authoring them
- URL: https://openalex.org/W2032587419

## 66. Pre-Grasp Sliding Manipulation of Thin Objects Using Soft, Compliant, or Underactuated Hands
- Year/venue: 2019 / IEEE Robotics and Automation Letters
- Problem claimed: We address the problem of pregrasp sliding manipulation, which is an essential skill when a thin object cannot be directly grasped from a flat surface.
- Actual mechanism introduced: planning representation or algorithm for robot action selection
- Hidden assumptions: manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2909622087

## 67. A gradient-based path optimization method for motion planning
- Year/venue: 2016 / Advanced Robotics
- Problem claimed: Most algorithms in probabilistic sampling-based path planning compute collision-free paths made of straight line segments lying in the configuration space.
- Actual mechanism introduced: sampling-based motion-space exploration
- Hidden assumptions: geometric feasibility can be recovered by more samples; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: motion-space search and narrow-passage exploration
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2320234922

## 68. Deep Reinforcement Learning for End-to-End Local Motion Planning of Autonomous Aerial Robots in Unknown Outdoor Environments: Real-Time Flight Experiments
- Year/venue: 2021 / Sensors
- Problem claimed: Autonomous navigation and collision avoidance missions represent a significant challenge for robotics systems as they generally operate in dynamic environments that require a high level of autonomy and flexible decision-making capabilities.
- Actual mechanism introduced: learned policy/model used inside planning
- Hidden assumptions: space remains navigable after local motion choices; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W3139779774

## 69. Planning human-aware motions using a sampling-based costmap planner
- Year/venue: 2011 / 
- Problem claimed: This paper addresses the motion planning problem while considering Human-Robot Interaction (HRI) constraints.
- Actual mechanism introduced: sampling-based motion-space exploration
- Hidden assumptions: geometric feasibility can be recovered by more samples; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: motion-space search and narrow-passage exploration
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2145313322

## 70. Cooperative Dynamic Motion Planning for Dual Manipulator Arms Based on RRT*Smart-AD Algorithm
- Year/venue: 2023 / Sensors
- Problem claimed: Intelligent manufacturing requires robots to adapt to increasingly complex tasks, and dual-arm cooperative operation can provide a more flexible and effective solution.
- Actual mechanism introduced: sampling-based motion-space exploration
- Hidden assumptions: geometric feasibility can be recovered by more samples; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: motion-space search and narrow-passage exploration
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4386608037

## 71. Pick and Place Operations in Logistics Using a Mobile Manipulator Controlled with Deep Reinforcement Learning
- Year/venue: 2019 / Applied Sciences
- Problem claimed: Programming robots to perform complex tasks is a very expensive job.
- Actual mechanism introduced: learned policy/model used inside planning
- Hidden assumptions: local action feasibility is sufficient for long-horizon planning; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2911426134

## 72. A Comprehensive Review on Autonomous Navigation
- Year/venue: 2022 / arXiv (Cornell University)
- Problem claimed: The field of autonomous mobile robots has undergone dramatic advancements over the past decades.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4312226162

## 73. Design and Motion Planning for a Reconfigurable Robotic Base
- Year/venue: 2022 / IEEE Robotics and Automation Letters
- Problem claimed: A robotic platform for mobile manipulation needs to satisfy two contradicting requirements for many real-world applications: A compact base is required to navigate through cluttered indoor environments, while the support needs to be large enough to prevent tumbling or tip over, especially during fast manipulation operations with heavy payloads or forceful interaction with the environment.
- Actual mechanism introduced: planning representation or algorithm for robot action selection
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4283775706

## 74. A Collaborative Robotic Approach to Autonomous Pallet Jack Transportation and Positioning
- Year/venue: 2020 / IEEE Access
- Problem claimed: This paper proposes a novel loco-manipulation control framework for the execution of complex tasks with kinodynamic constraints using mobile manipulators.
- Actual mechanism introduced: belief-state or uncertainty-aware planning
- Hidden assumptions: uncertainty is the main hidden variable; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: uncertainty-aware variants of planning
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W3046425165

## 75. Snake Robots for Surgical Applications: A Review
- Year/venue: 2022 / Robotics
- Problem claimed: Although substantial advancements have been achieved in robot-assisted surgery, the blueprint to existing snake robotics predominantly focuses on the preliminary structural design, control, and human–robot interfaces, with features which have not been particularly explored in the literature.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4229059846

## 76. Autonomous Quadruped Robot System with LiDAR Sensor Navigation and Task Execution
- Year/venue: 2025 / 
- Problem claimed: This study focuses on a project aimed at developing an autonomous system for a quadruped robot (Unitree B1).
- Actual mechanism introduced: planning representation or algorithm for robot action selection
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4411726342

## 77. Motion planning of multiple mobile robots for cooperative manipulation and transportation
- Year/venue: 2003 / IEEE Transactions on Robotics and Automation
- Problem claimed: In this paper, we propose a motion-planning method of multiple mobile robots for cooperative transportation of a large object in a three-dimensional environment.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2121837035

## 78. ChatGPT for Robotics: Design Principles and Model Abilities
- Year/venue: 2024 / IEEE Access
- Problem claimed: This paper presents an experimental study regarding the use of OpenAI’s ChatGPT [1] for robotics applications.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4394828156

## 79. Oceanic Challenges to Technological Solutions: A Review of Autonomous Underwater Vehicle Path Technologies in Biomimicry, Control, Navigation, and Sensing
- Year/venue: 2024 / IEEE Access
- Problem claimed: Autonomous Underwater Vehicles (AUVs) epitomize a revolutionary stride in underwater exploration, seamlessly assuming tasks once exclusive to manned vehicles.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4393033207

## 80. An Extensive Review of Mobile Agricultural Robotics for Field Operations: Focus on Cotton Harvesting
- Year/venue: 2020 / AgriEngineering
- Problem claimed: In this review, we examine opportunities and challenges for 21st-century robotic agricultural cotton harvesting research and commercial development.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W3009451162

## 81. CHOMP: Gradient optimization techniques for efficient motion planning
- Year/venue: 2009 / 
- Problem claimed: Existing high-dimensional motion planning algorithms are simultaneously overpowered and underpowered.
- Actual mechanism introduced: sampling-based motion-space exploration
- Hidden assumptions: geometric feasibility can be recovered by more samples; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution
- What it makes less novel: motion-space search and narrow-passage exploration
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2099893201

## 82. Augmented Reality for Robotics: A Review
- Year/venue: 2020 / Robotics
- Problem claimed: Augmented reality (AR) is used to enhance the perception of the real world by integrating virtual objects to an image sequence acquired from various camera technologies.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W3014471496

## 83. Dealing with Difficult Instances of Object Rearrangement
- Year/venue: 2015 / 
- Problem claimed: Rearranging multiple objects is a critical skill for robots so that they can effectively deal with clutter in human spaces.
- Actual mechanism introduced: object arrangement ordering and manipulation feasibility search
- Hidden assumptions: objects can be moved without creating unrecoverable access losses; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: planning around object-induced access constraints
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode; separate rearrangement ordering from reachability loss certificates
- URL: https://openalex.org/W2293698677

## 84. Task and Motion Informed Trees (TMIT*): Almost-Surely Asymptotically Optimal Integrated Task and Motion Planning
- Year/venue: 2022 / IEEE Robotics and Automation Letters
- Problem claimed: High-level autonomy requires discrete and continuous reasoning to decide both what actions to take and how to execute them.
- Actual mechanism introduced: integrated symbolic-geometric task/motion planning
- Hidden assumptions: symbolic predicates remain valid across geometric execution; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: integrating symbolic goals with geometric feasibility
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode; lift geometric dead-end cuts into symbolic preconditions without hand-authoring them
- URL: https://openalex.org/W4293769215

## 85. Assisted Teleoperation Strategies for Aggressively Controlling a Robot Arm with 2D Input
- Year/venue: 2011 / 
- Problem claimed: This paper studies assisted teleoperation techniques for controlling a 6DOF robot arm using click-and-drag input from a computer mouse.
- Actual mechanism introduced: planning representation or algorithm for robot action selection
- Hidden assumptions: local action feasibility is sufficient for long-horizon planning; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W1444114573

## 86. Bridging Requirements, Planning, and Evaluation: A Review of Social Robot Navigation
- Year/venue: 2024 / Sensors
- Problem claimed: Navigation lies at the core of social robotics, enabling robots to navigate and interact seamlessly in human environments.
- Actual mechanism introduced: planning representation or algorithm for robot action selection
- Hidden assumptions: space remains navigable after local motion choices; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4396219850

## 87. Optimizing Mobile Robot Navigation Based on A-Star Algorithm for Obstacle Avoidance in Smart Agriculture
- Year/venue: 2024 / Electronics
- Problem claimed: The A-star algorithm (A*) is a traditional and widely used approach for route planning in various domains, including robotics and automobiles in smart agriculture.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4399043196

## 88. A review of the challenges in mobile manipulation: systems design and RoboCup challenges
- Year/venue: 2020 / e+i Elektrotechnik und Informationstechnik
- Problem claimed: Abstract Mobile robotics is already well established in today’s production lines.
- Actual mechanism introduced: contact/action model for manipulation under geometric constraints
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W3083343096

## 89. Kinova Modular Robot Arms for Service Robotics Applications
- Year/venue: 2017 / International Journal of Robotics Applications and Technologies
- Problem claimed: This article presents Kinova's modular robotic systems, including the robots JACO2 and MICO2, actuators and grippers.
- Actual mechanism introduced: contact/action model for manipulation under geometric constraints
- Hidden assumptions: manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2783470107

## 90. Robotic manipulator motion planning method development using neural network-based intelligent system
- Year/venue: 2023 / 
- Problem claimed: The research relevance is determined by the constant development of industry and the use of robotic manipulators in production processes.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: local action feasibility is sufficient for long-horizon planning; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4391435629

## 91. Deep Learning for Robotics
- Year/venue: 2021 / Journal of Data Analysis and Information Processing
- Problem claimed: The application of deep learning to robotics over the past decade has led to a wave of research into deep artificial neural networks and to a very specific problems and questions that are not usually addressed by the computer vision and machine learning communities.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W3154362494

## 92. Actor-Critic Reinforcement Learning for Control With Stability Guarantee
- Year/venue: 2020 / IEEE Robotics and Automation Letters
- Problem claimed: Reinforcement Learning (RL) and its integration with deep learning have achieved impressive performance in various robotic control tasks, ranging from motion planning and navigation to end-to-end visual manipulation.
- Actual mechanism introduced: belief-state or uncertainty-aware planning
- Hidden assumptions: uncertainty is the main hidden variable; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: uncertainty-aware variants of planning
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W3045059767

## 93. A constraint-based method for solving sequential manipulation planning problems
- Year/venue: 2014 / 
- Problem claimed: In this paper, we describe a strategy for integrated task and motion planning based on performing a symbolic search for a sequence of high-level operations, such as pick, move and place, while postponing geometric decisions.
- Actual mechanism introduced: integrated symbolic-geometric task/motion planning
- Hidden assumptions: symbolic predicates remain valid across geometric execution; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: integrating symbolic goals with geometric feasibility
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode; lift geometric dead-end cuts into symbolic preconditions without hand-authoring them
- URL: https://openalex.org/W2031738727

## 94. Modeling of Deformable Objects for Robotic Manipulation: A Tutorial and Review
- Year/venue: 2020 / Frontiers in Robotics and AI
- Problem claimed: Manipulation of deformable objects has given rise to an important set of open problems in the field of robotics.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W3091248659

## 95. Geometrically constrained path planning for robotic grasping with Differential Evolution and Fast Marching Square
- Year/venue: 2022 / Robotica
- Problem claimed: Abstract This paper presents a new approach for geometrically constrained path planning applied to the field of robotic grasping.
- Actual mechanism introduced: planning representation or algorithm for robot action selection
- Hidden assumptions: manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4220892609

## 96. Hierarchical planning architectures for mobile manipulation tasks in indoor environments
- Year/venue: 2010 / 
- Problem claimed: This paper describes a hierarchical planner deployed on a mobile manipulation system.
- Actual mechanism introduced: planning representation or algorithm for robot action selection
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W1970857232

## 97. Navigation in the presence of humans
- Year/venue: 2006 / 
- Problem claimed: Robot navigation in the presence of humans raises new issues for motion planning and control since the humans safety and comfort must be taken explicitly into account.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2545274401

## 98. Hierarchical Policy Blending as Inference for Reactive Robot Control
- Year/venue: 2023 / 
- Problem claimed: Motion generation in cluttered, dense, and dynamic environments is a central topic in robotics, rendered as a multi-objective decision-making problem.
- Actual mechanism introduced: planning representation or algorithm for robot action selection
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4383108656

## 99. A mobile robot that performs human acceptable motions
- Year/venue: 2006 / 
- Problem claimed: The presence of humans should be explicitly taken into account in all steps of robot's design and particularly for robot motion.
- Actual mechanism introduced: planning representation or algorithm for robot action selection
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; world dynamics during planning; commitment cost model
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W2153120627

## 100. Chaotic Motion Planning for Mobile Robots: Progress, Challenges, and Opportunities
- Year/venue: 2023 / IEEE Access
- Problem claimed: Chaotic path planners are a subset of path planning algorithms that use chaotic dynamical systems to generate trajectories throughout an environment.
- Actual mechanism introduced: heuristic graph/search procedure
- Hidden assumptions: manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Variables treated as fixed: map/geometry; object identities; goal predicates; commitment cost model; external agents
- Failure modes ignored: a short motion can cut off an unserved future obligation; a placement/push can make a necessary region unreachable; dead-end commitments are detected only after search/execution; narrow-passage commitments are treated as ordinary geometry
- What it makes less novel: general planning/search framing
- What it leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode
- URL: https://openalex.org/W4389105004
