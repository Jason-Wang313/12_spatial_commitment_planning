# Literature Map

## Field box
Robotics planning for embodied agents that must navigate and manipulate in spatial environments where actions can change future reachability. The center of mass is task-and-motion planning, navigation among movable obstacles, object rearrangement, mobile manipulation, and sampling/heuristic motion planning.

## Sweep accounting
- Landscape sweep: 1000 ranked entries in `docs/related_work_matrix.csv`.
- Serious skim: top 300 entries by relevance score.
- Deep read: top 250 entries, using abstract/metadata-grounded extraction columns.
- Hostile prior-work set: top 100 entries most likely to reduce novelty.
- Year span in collected set: 1985-2025.

## Dominant mechanisms observed in the serious skim
- heuristic graph/search procedure: 101
- planning representation or algorithm for robot action selection: 74
- sampling-based motion-space exploration: 36
- integrated symbolic-geometric task/motion planning: 32
- learned policy/model used inside planning: 22
- belief-state or uncertainty-aware planning: 15
- contact/action model for manipulation under geometric constraints: 13
- search over obstacle rearrangements and navigation constraints: 3
- object arrangement ordering and manipulation feasibility search: 3
- symbolic search with sampled geometric streams: 1

## Query sources represented in the landscape
- `robot task and motion planning manipulation navigation`: 804
- `integrated task and motion planning robotics manipulation`: 196

## Hidden assumptions that may be false
1. Spatial actions are locally reversible unless the domain author explicitly marks them otherwise.
2. If a motion is geometrically feasible now, its long-horizon consequence can be postponed to later search.
3. A symbolic predicate such as at(room) captures the relevant spatial state for future planning.
4. A robot can return to a previous approach region after passing through a narrow passage.
5. Object placements are static facts rather than changes to the topology of future reachability.
6. Manipulation actions only change object poses, not the robot's future maneuvering options.
7. Dead ends are rare enough that backtracking search will discover them cheaply.
8. Reachability loss can be represented as ordinary action cost.
9. The set of future obligations is independent of the spatial boundary just crossed.
10. Roadmap or sampling density is the main reason a narrow passage is hard.
11. The planner can evaluate feasibility one subgoal at a time.
12. A learned or heuristic high-level agenda can be repaired after geometric failure.
13. Topological access is fixed during execution.
14. The relevant failure mode is uncertainty, not irreversible commitment under known geometry.
15. All preconditions worth reasoning about are attached to actions, not to spatial cuts.
16. Rearrangement constraints are object-ordering constraints only, not access-loss constraints.
17. The cost-to-go heuristic may ignore whether a necessary return path survives.
18. Execution monitors can catch commitment mistakes without needing to change the planner's state space.
19. Navigation and manipulation commitments can be handled by separate modules.
20. A future geometric plan exists if every local transition has an inverse somewhere in the roadmap.
21. The robot's body/cargo footprint does not turn a corridor traversal into a one-way commitment.
22. Deleting a reachable region is equivalent to increasing its traversal cost.
23. The planner need not expose why a branch became impossible.
24. A failure certificate after the fact is as useful as a commitment certificate before the fact.
25. Task-level abstractions can be complete without representing spatial accessibility basins.
26. The same symbolic state is valid on both sides of a one-way spatial boundary.

## Direction candidates that break assumptions
- **Commitment-cut planning.** Derive directed spatial cuts whose traversal deletes access to obligations; promote the cut and its outstanding obligations into the planning state.
- **Manipulation-mode foreclosure.** Track grasp, cargo, and placement choices as commitments that remove approach manifolds before a placement is made.
- **Reversible-region contracts.** Compile each local roadmap region into a contract saying which tasks remain reversible from that region.
- **Commitment-aware agenda repair.** Instead of validating an agenda, insert ordering constraints induced by impending access loss.
- **Spatial debt accounting.** Measure how many future obligations a partial plan owes before crossing each boundary.
- **Cut-derived symbolic predicates.** Generate PDDL-like predicates from geometric reachability cuts rather than hand-writing all dead-end preconditions.
- **Contact-as-topology planning.** Treat pushes and placements as topological edits to accessibility, not only continuous contact dynamics.
- **Commitment certificates for demonstrations.** Annotate robot demonstrations with the first point at which future alternatives are lost.

## Top hostile papers and what they leave open
### 1. Dexterous robotic motion planning using intelligent algorithms (2015)
- Problem claimed: The fundamental purpose of robots is to help humans in a variety of difficult tasks, enabling people to increase their capabilities of strength, energy, speed, memory, and to operate in hazardous environments and many other applications.
- Mechanism: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Makes less novel: general planning/search framing
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode

### 2. Constraint Graphs: Unifying task and motion planning for Navigation and Manipulation Among Movable Obstacles (2016)
- Problem claimed: We consider a class of advanced motion planning problems including object manipulation, navigation among movable obtacles and legged locomotion.
- Mechanism: integrated symbolic-geometric task/motion planning
- Hidden assumptions: symbolic predicates remain valid across geometric execution; geometric feasibility can be recovered by more samples; objects can be moved without creating unrecoverable access losses; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Makes less novel: integrating symbolic goals with geometric feasibility; planning around object-induced access constraints; motion-space search and narrow-passage exploration
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode; separate rearrangement ordering from reachability loss certificates; lift geometric dead-end cuts into symbolic preconditions without hand-authoring them

### 3. ManipulaTHOR: A Framework for Visual Object Manipulation (2021)
- Problem claimed: The domain of Embodied AI has recently witnessed substantial progress, particularly in navigating agents within their environments.
- Mechanism: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Makes less novel: general planning/search framing
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode

### 4. Linear manipulator: Motion control of an n-link robotic arm mounted on a mobile slider (2023)
- Problem claimed: Linear manipulators are versatile linear robotics systems that can be reprogrammed to accommodate product changes quickly and are flexible to meet unique requirements.
- Mechanism: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; irreversible spatial commitments are not explicit state variables
- Makes less novel: general planning/search framing
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode

### 5. Versatile multicontact planning and control for legged loco-manipulation (2023)
- Problem claimed: Loco-manipulation planning skills are pivotal for expanding the utility of robots in everyday environments.
- Mechanism: integrated symbolic-geometric task/motion planning
- Hidden assumptions: symbolic predicates remain valid across geometric execution; geometric feasibility can be recovered by more samples; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Makes less novel: integrating symbolic goals with geometric feasibility; motion-space search and narrow-passage exploration
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode; lift geometric dead-end cuts into symbolic preconditions without hand-authoring them

### 6. Homotopic Path Set Planning for Robot Manipulation and Navigation (2024)
- Problem claimed: This paper addresses path set planning that yields important applications in robot manipulation and navigation such as path generation for deformable object keypoints and swarms.A path set refers to the collection of finite agent paths to represent the overall spatial path of a group of keypoints or a swarm, whose collective properties meet spatial and topological constraints.As opposed to planning a single path, sim
- Mechanism: sampling-based motion-space exploration
- Hidden assumptions: geometric feasibility can be recovered by more samples; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Makes less novel: motion-space search and narrow-passage exploration
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode

### 7. Stability Analysis and Navigational Techniques of Wheeled Mobile Robot: A Review (2023)
- Problem claimed: Wheeled mobile robots (WMRs) have been a focus of research for several decades, particularly concerning navigation strategies in static and dynamic environments.
- Mechanism: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; irreversible spatial commitments are not explicit state variables
- Makes less novel: general planning/search framing
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode

### 8. M<sup>2</sup> Diffuser: Diffusion-based Trajectory Optimization for Mobile Manipulation in 3D Scenes (2025)
- Problem claimed: Recent advances in diffusion models have opened new avenues for research into embodied AI agents and robotics.
- Mechanism: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Makes less novel: general planning/search framing
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode

### 9. An Immunological Approach to Mobile Robot Navigation (2008)
- Problem claimed: Autonomous mobile robots have a wide range of applications in industries, hospitals, offices, and even the military, due to their superior mobility.
- Mechanism: belief-state or uncertainty-aware planning
- Hidden assumptions: uncertainty is the main hidden variable; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Makes less novel: uncertainty-aware variants of planning
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode

### 10. A review on indoor human aware autonomous mobile robot navigation through a dynamic environment survey of different path planning algorithm and methods (2015)
- Problem claimed: Practical realistic environment for path and continuous motion planning problems normally consist of numerous working areas such as in indoor application consist of number of bedrooms, hallways, multiple doorways with many static and dynamic obstacle in between.
- Mechanism: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Makes less novel: general planning/search framing
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode

### 11. Development of a Multifunctional Mobile Manipulation Robot Based on Hierarchical Motion Planning Strategy and Hybrid Grasping (2025)
- Problem claimed: A mobile manipulation robot combines the navigation capability of unmanned ground vehicles and manipulation advantage of robotic arms.
- Mechanism: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Makes less novel: general planning/search framing
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode

### 12. Motion planning with temporal-logic specifications: Progress and challenges (2015)
- Problem claimed: Integrating task and motion planning is becoming increasingly important due to the recognition that a growing number of robotics applications in navigation, search-and-rescue missions, manipulation, and medicine involve reasoning with both discrete abstractions and continuous motions.
- Mechanism: integrated symbolic-geometric task/motion planning
- Hidden assumptions: symbolic predicates remain valid across geometric execution; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Makes less novel: integrating symbolic goals with geometric feasibility
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode; lift geometric dead-end cuts into symbolic preconditions without hand-authoring them

### 13. A Survey of Robotic Harvesting Systems and Enabling Technologies (2023)
- Problem claimed: This paper presents a comprehensive review of ground agricultural robotic systems and applications with special focus on harvesting that span research and commercial products and results, as well as their enabling technologies.
- Mechanism: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Makes less novel: general planning/search framing
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode

### 14. Fast, Anytime Motion Planning for Prehensile Manipulation in Clutter (2018)
- Problem claimed: Many methods have been developed for planning the motion of robotic arms for picking and placing, ranging from local optimization to global search techniques, which are effective for sparsely placed objects.
- Mechanism: sampling-based motion-space exploration
- Hidden assumptions: geometric feasibility can be recovered by more samples; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Makes less novel: motion-space search and narrow-passage exploration
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode

### 15. Visibility-Aware Navigation Among Movable Obstacles (2023)
- Problem claimed: In this paper, we examine the problem of visibility-aware robot navigation among movable obstacles (VANAMO).
- Mechanism: search over obstacle rearrangements and navigation constraints
- Hidden assumptions: objects can be moved without creating unrecoverable access losses; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Makes less novel: planning around object-induced access constraints
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode

### 16. Perceptive Locomotion for Legged Robots in Rough Terrain (2018)
- Problem claimed: Robotic technologies will continue to enter new applications in addition to automated manufacturing and logistics.
- Mechanism: contact/action model for manipulation under geometric constraints
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Makes less novel: general planning/search framing
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode

### 17. Go Fetch: Mobile Manipulation in Unstructured Environments (2020)
- Problem claimed: With humankind facing new and increasingly large-scale challenges in the medical and domestic spheres, automation of the service sector carries a tremendous potential for improved efficiency, quality, and safety of operations.
- Mechanism: planning representation or algorithm for robot action selection
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Makes less novel: general planning/search framing
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode

### 18. Large language models for chemistry robotics (2023)
- Problem claimed: Abstract This paper proposes an approach to automate chemistry experiments using robots by translating natural language instructions into robot-executable plans, using large language models together with task and motion planning.
- Mechanism: symbolic search with sampled geometric streams
- Hidden assumptions: symbolic predicates remain valid across geometric execution; irreversible spatial commitments are not explicit state variables
- Makes less novel: integrating symbolic goals with geometric feasibility
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode; lift geometric dead-end cuts into symbolic preconditions without hand-authoring them

### 19. A Software Architecture for Service Robots Manipulating Objects in Human Environments (2020)
- Problem claimed: This paper presents a software architecture for robots providing manipulation services autonomously in human environments.
- Mechanism: integrated symbolic-geometric task/motion planning
- Hidden assumptions: symbolic predicates remain valid across geometric execution; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Makes less novel: integrating symbolic goals with geometric feasibility
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode; lift geometric dead-end cuts into symbolic preconditions without hand-authoring them

### 20. Mobile Robotic Manipulation for Search-and-Fetch Tasks by Integrating Human-Robot Interaction (2025)
- Problem claimed: The increasing labor shortages in commercial and industrial sectors have driven the development of mobile manipulation robots, which combine the mobility of mobile bases with the dexterity of robotic arms to automate complex tasks.
- Mechanism: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Makes less novel: general planning/search framing
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode

### 21. 3P-LLM: Probabilistic Path Planning using Large Language Model for Autonomous Robot Navigation (2024)
- Problem claimed: Much worldly semantic knowledge can be encoded in large language models (LLMs).
- Mechanism: sampling-based motion-space exploration
- Hidden assumptions: geometric feasibility can be recovered by more samples; space remains navigable after local motion choices; irreversible spatial commitments are not explicit state variables
- Makes less novel: motion-space search and narrow-passage exploration
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode

### 22. Towards Shared Autonomy Applications using Whole-body Control Formulations of Locomanipulation (2019)
- Problem claimed: While widely studied in robotics for decades, mobile manipulation has recently seen a surge in interest for industrial applications due to increasing demands on flexibility and agility alongside productivity, particularly in small and medium enterprises.
- Mechanism: planning representation or algorithm for robot action selection
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Makes less novel: general planning/search framing
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode

### 23. Autonomous live working robot navigation with real‐time detection and motion planning system on distribution line (2022)
- Problem claimed: Abstract In this study, an autonomous robot navigation system is designed for live working on distribution line.
- Mechanism: sampling-based motion-space exploration
- Hidden assumptions: geometric feasibility can be recovered by more samples; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Makes less novel: motion-space search and narrow-passage exploration
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode

### 24. Autonomous agents for real-time animation (1999)
- Problem claimed: Advances in computing hardware, software, and network technology have enabled a new class of interactive applications involving 3D animated characters to become increasingly feasible.
- Mechanism: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Makes less novel: general planning/search framing
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode

### 25. Learning compositional models of robot skills for task and motion planning (2021)
- Problem claimed: The objective of this work is to augment the basic abilities of a robot by learning to use sensorimotor primitives to solve complex long-horizon manipulation problems.
- Mechanism: integrated symbolic-geometric task/motion planning
- Hidden assumptions: symbolic predicates remain valid across geometric execution; geometric feasibility can be recovered by more samples; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Makes less novel: integrating symbolic goals with geometric feasibility; motion-space search and narrow-passage exploration
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode; lift geometric dead-end cuts into symbolic preconditions without hand-authoring them

### 26. Rigid body dynamics simulation for robot motion planning (2006)
- Problem claimed: The development of robot motion planning algorithms is inherently a challenging task.
- Mechanism: sampling-based motion-space exploration
- Hidden assumptions: geometric feasibility can be recovered by more samples; uncertainty is the main hidden variable; space remains navigable after local motion choices; irreversible spatial commitments are not explicit state variables
- Makes less novel: motion-space search and narrow-passage exploration; uncertainty-aware variants of planning
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode

### 27. Robotic Swarm Motion Planning for Load Carrying and Manipulating (2020)
- Problem claimed: Certain species of ants can carry out tasks in dense work spaces while maintaining their ability to accurately manipulate heavy loads, and these advantages are of interest to the robotics community.
- Mechanism: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; irreversible spatial commitments are not explicit state variables
- Makes less novel: general planning/search framing
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode

### 28. Path Smoothing Techniques in Robot Navigation: State-of-the-Art, Current and Future Challenges (2018)
- Problem claimed: Robot navigation is an indispensable component of any mobile service robot.
- Mechanism: heuristic graph/search procedure
- Hidden assumptions: space remains navigable after local motion choices; irreversible spatial commitments are not explicit state variables
- Makes less novel: general planning/search framing
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode

### 29. Visually Grounded Task and Motion Planning for Mobile Manipulation (2022)
- Problem claimed: Task and motion planning (TAMP) algorithms aim to help robots achieve task-level goals, while maintaining motion-level feasibility.
- Mechanism: integrated symbolic-geometric task/motion planning
- Hidden assumptions: symbolic predicates remain valid across geometric execution; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Makes less novel: integrating symbolic goals with geometric feasibility
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode; lift geometric dead-end cuts into symbolic preconditions without hand-authoring them

### 30. Skill Transformer: A Monolithic Policy for Mobile Manipulation (2023)
- Problem claimed: We present Skill Transformer, an approach for solving long-horizon robotic tasks by combining conditional sequence modeling and skill modularity.
- Mechanism: object arrangement ordering and manipulation feasibility search
- Hidden assumptions: objects can be moved without creating unrecoverable access losses; space remains navigable after local motion choices; manipulation choices do not permanently remove future approach modes; irreversible spatial commitments are not explicit state variables
- Makes less novel: planning around object-induced access constraints
- Leaves open: represent irreversible spatial commitments as reusable first-class planning objects; derive obligation cuts before committing to a corridor, placement, or manipulation mode; separate rearrangement ordering from reachability loss certificates
