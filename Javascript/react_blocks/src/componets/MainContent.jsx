import Subcontent from './Subcontent';
import Advertisment from './Advertisement';


const blocks = ["", "", ""];
const MainContent = () => {
    return (
        <div className="main">
            <div className='subcontent'>
            {blocks.map((block, index) => (
                <Subcontent key={index} />
            ))}
            </div>
            <Advertisment/>
        </div>
    );
};
export default MainContent;

