
const Delete = (props) => {
    const { currentTask, onDeleteTask, onToggleComplete } = props;

    const removeTask = (index) => {
        onDeleteTask(index);
    };

    const toggleComplete = (index) => {
        onToggleComplete(index);
    };

    return (
        <div className="delete">
            <ul>
                {currentTask.map((task, index) => (
                    <li key={index}>
                        <span style={{ textDecoration: task.startsWith('✓') ? 'line-through' : 'none' }}>{task}</span>
                        <input
                            type="checkbox"
                            checked={task.startsWith('✓')}
                            onChange={() => toggleComplete(index)}
                        />
                        <button onClick={() => removeTask(index)}>Delete</button>
                    </li>
                ))}
            </ul>
        </div>
    );
};

export default Delete;
