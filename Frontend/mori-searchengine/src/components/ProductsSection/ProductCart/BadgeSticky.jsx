export default function BadgeSticky({percent}) {
    return(
        <badge className="percent sticky">
            {percent}%
        </badge>
    );
}