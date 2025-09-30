 document.addEventListener('DOMContentLoaded', () => {
        const addButton = document.querySelector('.add');
        const contentHolder = document.getElementById('contentHolder');
        addButton.addEventListener('click',()=>{
            contentHolder.innerHTML+=`<div class="contentBox">
                <div class="title">
                    <h3>$TaskName$</h3>
                    <h3>-$TeamName$</h3>
                </div>
                <div class="progressBar">
                    <div class="progress"></div>
                </div>
                <div class="numericData">
                    <h6>$Time Remaining$</h6>
                    <h6>$Progress$</h6>
                </div>
                <div class="extraContent">
                    <hr>
                    <div>
                        <div class="taskDetails">
                            <p>Task Description: $Description$</p>
                            <p>Progress: $Progress$</p>
                            <p>Remaining: $Remaining$</p>
                        </div>
                        <div class="peopleDetails">
                            <div class="peopleWorking">People Working: $People Working$</div>
                            <div class="assignedBy">Assigned By: $Assigned By$</div>
                        </div>
                    </div>
                </div>
            </div>`
            
            // Add click event listener to the newly created content box
            addToggleEventListeners();
        });
        
        // Function to add toggle event listeners to all content boxes
        function addToggleEventListeners() {
            const contentBoxes = document.querySelectorAll('.contentBox');
            contentBoxes.forEach(box => {
                // Remove existing event listeners to prevent duplicates
                box.removeEventListener('click', toggleExtraContent);
                // Add new event listener
                box.addEventListener('click', toggleExtraContent);
            });
        }
        
        // Function to toggle extra content visibility
        function toggleExtraContent(event) {
            const extraContent = this.querySelector('.extraContent');
            if (extraContent) {
                if (extraContent.style.display === 'none' || extraContent.style.display === '') {
                    extraContent.style.display = 'block';
                } else {
                    extraContent.style.display = 'none';
                }
            }
        }
        
        // Initialize event listeners for any existing content boxes
        addToggleEventListeners();
    }); 
